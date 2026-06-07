#!/usr/bin/env python3
"""embed-covers.py — 把档案 HTML 里的 Open Library 外链封面下载并内联为 base64 data URI。

为什么需要：covers.openlibrary.org 现已对每一条封面请求 302 跳转到 archive.org
（再跳到 ia*.us.archive.org 从 zip 包里现解压），该链路慢且在中国大陆被屏蔽/限速。
外链封面在国内读者浏览器里加载失败，onerror 触发后只剩 .cover__fallback 书名色块。
生成时把封面下载并内联成 base64，档案即自包含：读者打开不再需要任何网络，国内/离线/永久可看。

用法:
    python3 embed-covers.py <archive.html> [<archive.html> ...]

行为：就地改写文件；下载失败的封面保留外链（配合 HTML 里 <img> 的 onerror+fallback 优雅降级）。
注意：若生成档案的机器本身连不上封面源（如国内直连），封面无法内联，会保留外链由 onerror 兜底。
依赖：python3 标准库 + curl（跟随 302 跳转链最稳）。
"""
import sys
import re
import base64
import shutil
import subprocess

# Open Library 封面外链，尺寸后缀 S/M/L 都兜住
URL_RE = re.compile(r'https://covers\.openlibrary\.org/b/id/\d+-[SML]\.jpg')


def fetch(url):
    """下载封面字节；跟随跳转，校验是真 JPEG 才返回，否则 None。
    -A 伪装常规 UA：archive.org 对无 UA 的请求偶尔返回错误页，并非安全用途。"""
    try:
        out = subprocess.run(
            ["curl", "-sL", "--max-time", "40", "-A", "Mozilla/5.0", url],
            capture_output=True, timeout=60,
        )
        data = out.stdout
        # JPEG 魔数 FF D8，且体积够大（排除 302 占位/错误页/截断）
        if len(data) > 1200 and data[:2] == b"\xff\xd8":
            return data
    except Exception:
        pass
    return None


def process(path):
    """处理单个文件。返回 True=文件读写正常（封面取不到不算文件级失败），False=文件 I/O 出错。"""
    try:
        with open(path, encoding="utf-8") as f:
            html = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"{path}: 读不到或不是文本文件，跳过（{e.__class__.__name__}）")
        return False
    urls = sorted(set(URL_RE.findall(html)))
    if not urls:
        print(f"{path}: 未发现外链封面（可能已内联或无封面）")
        return True
    ok = fail = 0
    for url in urls:
        data = fetch(url)
        if data:
            datauri = "data:image/jpeg;base64," + base64.b64encode(data).decode()
            html = html.replace(url, datauri)  # 同一 URL 多处出现一并替换
            ok += 1
        else:
            fail += 1
            print(f"  ✗ 取不到，保留外链（靠 onerror 兜底）: {url}")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
    except OSError as e:
        print(f"{path}: 写入失败（{e.__class__.__name__}），原文件未改动")
        return False
    print(f"{path}: 内联 {ok} 张，失败 {fail} 张")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("用法: python3 embed-covers.py <archive.html> ...")
    if shutil.which("curl") is None:
        sys.exit("需要 curl（下载封面、跟随 302 跳转），请先安装后重试。")
    all_ok = True
    for p in sys.argv[1:]:
        try:
            if not process(p):
                all_ok = False
        except Exception as e:  # 一个文件出错不影响其余文件
            all_ok = False
            print(f"{p}: 处理出错，跳过（{e.__class__.__name__}: {e}）")
    sys.exit(0 if all_ok else 1)
