#!/usr/bin/env bash
set -euo pipefail

# ── University skill · 跨平台一键安装 ───────────────────────────────
# 本地:  ./install.sh
# 远程:  curl -fsSL https://raw.githubusercontent.com/junjieashan/university-skill/main/install.sh | bash
# 把 skills/university/ 装到 Claude Code (~/.claude/skills) 和/或 Codex (~/.agents/skills)。

SKILL="university"
REPO="https://github.com/junjieashan/university-skill"

# 定位 skill 源：本地运行用脚本目录；curl|bash 运行则临时 clone
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"
if [ -n "${SCRIPT_DIR:-}" ] && [ -d "$SCRIPT_DIR/skills/$SKILL" ]; then
  SRC="$SCRIPT_DIR/skills/$SKILL"
else
  echo "→ 拉取 $SKILL …"
  TMP="$(mktemp -d)"
  git clone --depth 1 "$REPO" "$TMP/repo" >/dev/null 2>&1 || { echo "✗ git clone 失败"; exit 1; }
  SRC="$TMP/repo/skills/$SKILL"
fi
[ -d "$SRC" ] || { echo "✗ 找不到 skill 源目录: $SRC"; exit 1; }

install_to() {
  local dest="$1" label="$2"
  mkdir -p "$dest"
  rm -rf "$dest/$SKILL"
  cp -R "$SRC" "$dest/$SKILL"
  echo "✓ $label ← $dest/$SKILL"
}

found=0
if [ -d "$HOME/.claude" ]; then install_to "$HOME/.claude/skills" "Claude Code"; found=1; fi
if [ -d "$HOME/.codex" ] || [ -d "$HOME/.agents" ]; then install_to "$HOME/.agents/skills" "Codex"; found=1; fi

if [ "$found" -eq 0 ]; then
  cat <<EOF
未检测到 Claude Code (~/.claude) 或 Codex (~/.agents / ~/.codex)。
手动安装二选一：
  1) 把  skills/$SKILL/  复制到你的 agent 的 skills 目录；
  2) 在项目 AGENTS.md 里引用本仓库的  skills/$SKILL/SKILL.md 。
EOF
  exit 0
fi

echo
echo "完成 ✦ Claude Code 里运行 /reload-plugins，或重启 Codex，然后说「我想系统学 X」即可。"
