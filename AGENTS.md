# University Skill — Agent 指南

> 这个仓库是一个**跨平台 AI agent skill**：「大学 / university」。给它一个学科，它产出一份分阶段、可交互的学习路线档案——每个阶段学什么、配哪本书、现在该去找哪一本。

## 给支持 AGENTS.md 的工具（Codex / Cursor / Aider / Windsurf / Gemini CLI / Copilot 等）

这个 skill 的完整能力定义在 **[`skills/university/SKILL.md`](skills/university/SKILL.md)**。

当用户说「我想系统学 X」「系统学 X」「帮我规划 X 的学习路线」「找 X 的核心教材 / 书单」时，按该文件的流程执行：

1. 解析用户的领域与目标（提示词优先，模糊才简要追问）；
2. 检索顶尖大学本科培养方案 + 专业学会课程体系，建课程骨架；
3. 每门课交叉验证核心教材（≥2 本，带采用证据）；
4. 产出分阶段学习路线档案（阶段 → 课 → 配书 + 进度表 + 选书权衡）。

详见 SKILL.md 与 `skills/university/references/`。

## 安装

见 [`README.md`](README.md)，或运行 `./install.sh`（自动检测 Claude Code / Codex 并放到对应位置）。
