<p align="center">
  <img src="assets/logo.svg" alt="intern-skill" width="160">
</p>

<h1 align="center">intern-skill</h1>

<p align="center">
  一个陪你接手、读懂、调研并扩展开源项目的 AI 实习生。
</p>

<p align="center">
  <a href="README.en.md">English</a>
</p>

## 定位

intern-skill 是一个面向 Codex、Claude Code、Hermes Agent、OpenClaw 等 Agent 平台的项目学习与技术调研 Skill。

很多人第一次接手项目时，真正痛苦的不是“不会看某一行代码”，而是不知道项目入口在哪里、主链路怎么跑、哪些模块重要、哪些细节可以先跳过。README 看完还是一团乱，直接问 AI 又容易得到一大段泛泛解释。

intern-skill 的目标是把陌生项目变成一张可以推进的学习地图。你给它一个 GitHub 仓库或本地项目，它会先做项目 onboarding：识别技术栈、入口文件、依赖配置、核心模块、数据流和主执行路径，再根据你的基础逐步讲解。进入学习后，它会直接给出下一步学习建议和推荐顺序，不会像传统 AI 一样把“你想先看哪里”反复丢回给你。

它的亮点不是单纯“解释代码”，而是把源码阅读、环境诊断、主链路追踪、前沿技术调研、项目审计和发布准备组织成一套可复用的项目学习工作流。

它由一组按需启用的专业实习生组成：

- **项目导航实习生**：先建立项目定位、模块地图、主链路和学习优先级，让你知道从哪里开始。
- **基础助教实习生**：当你是小白或不熟悉技术栈时，先解释必要名词、背景知识和最小心智模型。
- **环境配置实习生**：下载项目、识别依赖、检查启动命令、生成环境诊断和最小运行建议。
- **技术调研实习生**：从项目里提取关键技术点，联网调研最新论文、热门开源项目、benchmark 和工具，再判断是否值得迁移。
- **质量审计实习生**：检查测试覆盖、数据流、日志、监控、异常处理和可靠性风险。
- **项目评审主管**：用独立视角随机抽查项目，不只问你刚学过的内容，也覆盖未探索模块和证据链。
- **发布准备实习生**：在上传 GitHub 前检查 README、license、敏感文件、大文件、远程仓库和安装说明。
- **职业表达实习生**：只有当你明确需要求职、面试、简历或作品集时，才把学习成果整理成可表达的项目经验。

## 适用人群

- **刚拿到项目无从下手的实习生**：先建立项目地图，再沿主链路学习。
- **想快速学习项目的求职者**：在理解项目后，再按需整理面试表达或作品集材料。
- **想扩展项目功能的开发者**：先判断新功能应该接在哪个模块，再规划最小实验。
- **刚接触某个技术栈的新手**：先解释必要概念，再进入代码。
- **需要评审或答辩练习的人**：模拟项目主管或老师，随机挑重点提问。

## 怎么使用

学习 GitHub 项目：

```text
用 intern-skill 学习这个项目：https://github.com/NousResearch/hermes-agent
```

学习本地项目：

```text
用 intern-skill 学习当前项目，先帮我建立项目地图，并直接给出下一步学习建议
```

基础助教实习生：

```text
我是小白，先解释这个项目里的 tool call、memory、skill 是什么
```

继续学习某个模块：

```text
继续学习 AIAgent.run_conversation 主循环，只讲这一段
```

项目评审主管：

```text
像项目主管一样随机问我 5 个问题，先不要给答案
```

环境配置实习生：

```text
检查这个项目的运行环境还缺什么
```

发布准备实习生：

```text
帮我发布这个项目到 GitHub，先做发布前检查
```

技术调研实习生：

```text
分析这个项目，选一个值得研究的技术点，调研最新相关项目和论文，判断哪些真正值得借鉴
```

## 一键部署

克隆本仓库后，在项目目录里运行：

```bash
bash scripts/install.sh --platform codex
```

可选平台：

```bash
bash scripts/install.sh --platform codex
bash scripts/install.sh --platform claude
bash scripts/install.sh --platform hermes
bash scripts/install.sh --platform openclaw --openclaw-project /path/to/miniOpenClaw-main
```

全部安装：

```bash
bash scripts/install.sh --platform all --openclaw-project /path/to/miniOpenClaw-main
```

如果目标目录已存在：

```bash
bash scripts/install.sh --platform codex --force
```

从 GitHub 远程一键安装：

```bash
PROJECT_INTERN_REPO_URL=https://github.com/aluochiyou/intern-skill.git \
  bash -c "$(curl -fsSL https://raw.githubusercontent.com/aluochiyou/intern-skill/main/scripts/install.sh)" -- --platform codex
```

## 扩展实习生

这些模块不会默认开启。你需要时，直接说出来就可以。

| 模块 | 适合什么时候用 | 示例 |
| --- | --- | --- |
| **技术调研实习生** | 最重要的拓展模块。它会从你的项目中提取关键技术点，联网调研最新论文、热门项目、benchmark 和工具，并判断哪些真正值得迁移 | `分析这个项目的技术点，找最新前沿启发` |
| **项目导航实习生** | 刚拿到项目，需要项目地图、主链路和学习顺序 | `先建立项目地图，并告诉我下一步学什么` |
| **基础助教实习生** | 不熟悉技术栈、术语或基础概念 | `我是小白，先讲必要概念` |
| **环境配置实习生** | 下载项目、识别技术栈、检查依赖、生成启动报告 | `帮我下载并检查怎么运行` |
| **质量审计实习生** | 检查测试覆盖、数据流、日志、风险点和可靠性问题 | `审计这个项目的数据流和测试覆盖` |
| **项目评审主管** | 模拟优秀项目主管或评审老师，随机抽查主链路、模块设计、风险和未学习区域 | `像项目主管一样问我 5 个问题` |
| **发布准备实习生** | 发布前检查 README、license、敏感文件、远程仓库和大文件 | `先做 GitHub 发布前检查` |
| **职业表达实习生** | 只有当你明确需要求职、面试、简历或作品集表达时才开启 | `整理成面试表达和简历可写点` |

其中，项目评审主管会尽量使用独立视角重新抽查项目，而不是只围绕你刚学过的内容提问。这样可以避免记忆偏置，补上还没有被检查过的模块、命令、数据流和风险点。

## 自我成长

intern-skill 像一个真正的实习生一样不断学习成长。

它会同步你的学习进度与能力，逐渐形成一个和你水平相匹配的项目助手：你已经掌握的内容，它会少讲；你还没建立概念的地方，它会先补基础；你可以理解但还没熟练的模块，它会用更小的任务继续推进。

这种自我成长不是盲目增加功能，而是通过项目地图、学习日志、反馈记录和评测结果，持续校准讲解深度、提问难度、下一步学习路线和调研方向。它的目标是减少无效解释，让每次学习都更贴近你当前的理解水平。

你可以在学习一段时间后这样说：

```text
根据我这次学习的情况，帮我调整 intern-skill 的讲解方式
```

它会检查：

- 当前讲解是否符合你的基础。
- 有没有重复讲你已经掌握的内容。
- 有没有跳过必要概念。
- 一次推进的内容是否太多。
- 下一步学习建议是否清楚。

如果需要改进，它会先提出一个小的调整建议，等你确认后再更新 Skill。

## 安装位置

| 平台 | 默认位置 |
| --- | --- |
| Codex | `~/.codex/skills/project-intern` |
| Claude Code | `~/.claude/skills/project-intern` |
| Hermes Agent | `$HERMES_HOME/skills/project-intern`，默认 `~/.hermes/skills/project-intern` |
| OpenClaw / miniOpenClaw | `<project>/backend/skills/project-intern` |

Hermes Agent 安装后，如果会话已经在运行，可以执行：

```text
/reload-skills
```

## 检查

发布或分发前运行：

```bash
python scripts/check_package.py
```

## 目录结构

```text
intern-skill/
├── README.md
├── README.en.md
├── assets/
│   └── logo.svg
├── scripts/
│   ├── install.py
│   ├── install.sh
│   └── check_package.py
└── skills/
    └── project-intern/
        ├── SKILL.md
        ├── references/
        └── scripts/
```

## License

MIT
