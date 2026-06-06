# 来源分级注册表（活文档：新来源随用随补，过时来源标注退役）

> 方法论出处：`资料来源/translation.md`（教科书书单 Agent 数据源盘点，2026-06 译）。
> 铁律：**每级来源只能定它有资格定的结论**，越级采信 = 把三手意见当一手证据。

## 全局约束

**禁止使用任何中文网站作为信息来源**（包括豆瓣、知乎、微信公众号、中文博客、中国高校官网等）。
唯一例外：T5 中译本查询可用豆瓣读书核实书名，但不作为推荐依据。

## 分级总表

| 级 | 来源类型 | 能定 | 不能定 |
|---|---|---|---|
| T1 | 学会课程体系 | 课程骨架、主题覆盖、核心能力 | 书名（学会文件刻意不推荐教材） |
| T2 | 一手课程大纲/培养方案 | 谁在用哪本书（描述性信号）、课程单元切分 | 阅读顺序、版本优劣 |
| T3 | 规范性精选书单 | 顺序、梯度、版本对比、编辑评注 | 单独定"公认"（有编辑偏好） |
| T4 | 社区讨论 | 佐证 T2/T3 结论、提示遗漏候选 | 任何定案 |
| T5 | 书目解析 | 版次、年份、ISBN、中译本 | 推荐与否 |

## T1 学会课程体系

| 领域 | 来源 | 入口 |
|---|---|---|
| 计算机 | ACM/IEEE CS2023（伞框架 CC2020；另有 IS2020/CCDS2021/CSEC2017） | csed.acm.org |
| 数学 | MAA CUPM Curriculum Guide 2015 | maa.org/cupm |
| 统计 | ASA GAISE College Report 2016 | amstat.org |
| 心理 | APA Undergraduate Psychology Major Guidelines 3.0 (2023) | apa.org |
| 生物 | AAAS Vision and Change (2011) | — |
| 生化 | ASBMB core concepts | asbmb.org |
| 化学 | ACS Guidelines for Bachelor's Degree Programs (2023) | — |
| 神经科学 | SfN / FUN Core Competencies for Neuroscience Undergraduates | FUN: JUNE 2012 开放获取 |
| 物理 | AAPT 实验课程建议 2014；AAPT+APS Phys21 (2016，技能框架) | — |
| 哲学/政治学 | **无学会课程体系** → 退用 3-5 所 top 校培养方案交叉 | — |

注意：学会文件几乎从不指定教材（GAISE 原话："本报告的建议并非关于如何选书"）——T1 只供骨架。

## T2 一手课程大纲 / 培养方案

**通用强校 + 领域特长校（4-6 所）：**

| 通用 | 领域特长示例 |
|---|---|
| MIT（OCW 全公开，首选） | 神经科学：JHU, UCSD, UCL |
| Stanford / Harvard / Berkeley | 经济学：Chicago, LSE |
| Oxford / Cambridge | CS/AI：CMU, Berkeley |
| | 物理：Caltech, Princeton；心理：Michigan, Penn |

**高价值入口：**
- MIT OCW（ocw.mit.edu）：课程页带 syllabus + 教材，最易 fetch
- 各校 syllabus 库：UCSD `courses.ucsd.edu/syllabiList.aspx`（官方 PDF 存档，本项目已验证可用）
- 剑桥数学 Tripos "Guide to Courses"（maths.cam.ac.uk/undergrad）：官方大纲+推荐教材+出版社，PDF
- 牛津学院 reading list（如 Balliol）：科目书单 HTML
- Open Yale Courses（oyc.yale.edu）：~40 门文理导论课带书单
- 美国高校课程表（HEOA 法案强制公开 ISBN）：`{school}.bncollege.com/course-material/course-finder` 可按校查课程教材——按需用，无聚合器
- 培养方案：`<学校> <专业> major requirements` 到院系官网

**范围限制：仅查英语授课院校**（US/UK/AU 等），中文培养方案/中文大纲不作 T2 来源——
中国高校教材体系与英语体系独立，混用会污染双信号交叉结果。

**使用要求：**深检索必须 WebFetch 原文确认 required/recommended 字段；记录学校+课号+学期/年+链接。

## T3 规范性精选书单

| 领域 | 书单 | 特点 |
|---|---|---|
| CS | teachyourselfcs.com | 9 科目 × 每科 1 本经典 + 视频课，最权威 CS 精选 |
| CS/数据/数学/生信 | OSSU（github.com/ossu） | 按 ACM/IEEE 指南组织的完整自学课程 + readings |
| 物理/数学/哲学 | Susan Rigetti 自学指南（susanrigetti.com） | 带版次、必读/补充标签、本科→研究生顺序 |
| 数学 | Chicago UG Math Bibliography（github.com/ystael/chicago-ug-math-bib） | 按子领域+难度的带注书目，含横向对比 |
| 数学 | rossant/awesome-math 等 awesome-* | 质量参差，需双信号过滤 |
| 物理/数学 | Stack Exchange big-lists（[resource-recommendations]/[books] 标签） | 社区共识沉淀，按 tag/score 可查 |
| 人文 | 圣约翰学院 Great Books list（sjc.edu） | 原典经典，非 STEM 教材体系 |

**使用要求：**记录书单名+链接+其给出的顺序/梯度意见；T3 单独命中只能进候选位。

## T4 社区讨论（只佐证）

- Reddit 学科子版 FAQ/wiki（r/learnmath、r/Physics、r/neuroscience…）
- 学科论坛、Goodreads、对比类博文（如 Neuroamer 教材对比）
- **时效教训（2026-06 实例）**：Neuroamer 2016 称 Berkeley 用 Kandel，实际 MCB 160
  现行 required 已换 Luo。对比长文常年不更新——T4 只用来佐证和提示遗漏，凡与 T2 冲突以 T2 为准。

## T5 书目解析

- Google Books API / books.google.com：模糊书名 → 版次/ISBN
- Open Library（openlibrary.org）：版本谱系、出版年
- 出版社页（最权威版次信息）：Norton/McGraw-Hill/OUP/Jones & Bartlett/Springer…
- 中译本：豆瓣读书 / 出版社中文站搜书名

## 退役/受限来源（别依赖）

- WorldCat 免费 Search API：2024 年底已停
- Open Syllabus：无公开 API，免费工具在 Cloudflare 后面；若其 CC-NC 批量数据集发布（已宣布），可升级为 T2 级描述性主干
- MERLOT（付费 key）、OER Commons（仅 LTI）：暂不接入
