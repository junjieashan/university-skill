<div align="center">

# 🎓 大学 · University

**给 AI 一个学科，换回一张「学到通」的路线图。**

输入一个领域，它检索全球顶尖大学的培养方案与专业学会课程体系，产出一份**分阶段、可交互**的学习路线档案——每个阶段学什么、配哪本书、现在该去找哪一本，一屏看清。

适配 **Claude Code · Codex · 开源 agent** ｜ [安装](#-安装) · [用法](#-用法) · [在线体验](https://junjieashan.github.io/university-skill/examples/philosophy.html)

</div>

---

![大学 · 横向节点路线图](assets/preview-routemap.png)

## ✨ 它解决什么

自学一个陌生领域，最大的摩擦从来不是找不到资料，而是：

- **不知道按什么顺序学** —— 一上来啃了太难的，挫败放弃；
- **不知道读哪本书** —— 同一门课十几本教材，哪本不预设基础、适合我？
- **学着学着没了方向感** —— 不知道学到哪了、下一步是什么。

`university` 把这三件事一次解决：一张**可溯源**的「该学什么 → 读哪本 → 什么顺序 → 现在去找什么」地图，每一处声称都链到真实的大学课程页。

## 📚 产出长什么样

上图是「哲学」领域的真实产出。两块核心：

**① 第一屏 · 横向节点路线图**（见上图）—— 4 个阶段串成一条线，每门课列出全部书，点阶段 / 点书名直接跳到详情。

**② 竖向书目时间轴** —— 每门课主选书 + 备选书分列中轴两侧，封面 / 作者 / 出版社 / 哪些大学在用都在；阶段用框线圈起，滚动时中轴随进度填充。

![大学 · 竖向书目时间轴](assets/preview-timeline.png)

> 🔗 **在线体验**（可滚动、点击跳转、阶段高亮）：<https://junjieashan.github.io/university-skill/examples/philosophy.html>

## 🚀 安装

skill 的本体是一份 `SKILL.md`——Claude Code 和 Codex 都**原生支持**，开源 agent 通过 `AGENTS.md` 兼容。

### 一键脚本（自动检测工具）

```bash
curl -fsSL https://raw.githubusercontent.com/junjieashan/university-skill/main/install.sh | bash
```

自动装到 Claude Code（`~/.claude/skills/`）和 / 或 Codex（`~/.agents/skills/`）。

### Claude Code（marketplace）

```
/plugin marketplace add junjieashan/university-skill
/plugin install university@university
/reload-plugins
```

### Codex

```bash
git clone https://github.com/junjieashan/university-skill
cp -r university-skill/skills/university ~/.agents/skills/
```

### 其他 agent（Cursor · Aider · Windsurf · Gemini CLI …）

仓库自带 `AGENTS.md`，认这个开放标准的工具会自动读到 skill 摘要与指向 `skills/university/SKILL.md` 的入口。

## 💡 用法

```
/university 我想系统学习哲学
```

给一句话目标即可。口径模糊时它会简要追问（通识打底还是攻某流派），然后检索、选书、生成档案。

## 🧩 它属于 Eatbook

`university` 是 [Eatbook](https://github.com/junjieashan)「最小摩擦的彻底理解」阅读系统的第一步——选好书、排好路线之后，还有入库、深读、共读、分支深研。

---

<div align="center">
<sub>MIT License · by <a href="https://github.com/junjieashan">junjieashan</a></sub>
</div>
