<p align="center">
  <img src="assets/logo.svg" alt="Intern Skill" width="160">
</p>

<h1 align="center">Intern Skill</h1>

<p align="center">
  一个陪你接手、读懂、扩展开源项目的 AI 实习生。
</p>

<p align="center">
  <a href="README.en.md">English</a>
</p>

## 定位

Intern Skill 是一个面向 Codex、Claude Code、Hermes Agent、OpenClaw 等 Agent 平台的项目学习 Skill。

你给它一个 GitHub 仓库或本地项目，它会先帮你看清项目是做什么的、从哪里开始读、主链路怎么走，再根据你的水平一点点讲清楚代码。它不是一次性把所有文件倒给你，而是像一个有耐心的实习生搭档，陪你把陌生项目拆成可以理解的小块。

它可以帮你完成从“刚拿到项目，不知道看哪里”到“我知道主流程、核心模块和下一步该学什么”的过渡。

## 适用人群

- **刚拿到项目无从下手的实习生**：先建立项目地图，再沿主链路学习。
- **想快速学习项目的求职者**：在理解项目后，再按需整理面试表达或作品集材料。
- **想扩展项目功能的开发者**：先判断新功能应该接在哪个模块，再规划最小实验。
- **刚接触某个技术栈的新手**：先解释必要概念，再进入代码。
- **需要评审或答辩练习的人**：模拟项目主管或老师，随机挑重点提问。

## 怎么使用

学习 GitHub 项目：

```text
用 Intern Skill 学习这个项目：https://github.com/NousResearch/hermes-agent
```

学习本地项目：

```text
用 Intern Skill 学习当前项目，先帮我建立项目地图
```

小白模式：

```text
我是小白，先解释这个项目里的 tool call、memory、skill 是什么
```

继续学习某个模块：

```text
继续学习 AIAgent.run_conversation 主循环，只讲这一段
```

随机提问：

```text
像项目主管一样随机问我 5 个问题，先不要给答案
```

环境检查：

```text
检查这个项目的运行环境还缺什么
```

GitHub 发布准备：

```text
帮我发布这个项目到 GitHub，先做发布前检查
```

前沿技术雷达：

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

## 扩展模块

这些模块不会默认开启。你需要时，直接说出来就可以。

| 模块 | 适合什么时候用 | 示例 |
| --- | --- | --- |
| 小白模式 | 不熟悉技术栈或术语 | `我是小白，先讲必要概念` |
| 环境配置 | 下载项目、检查依赖、生成启动报告 | `帮我下载并检查怎么运行` |
| 随机提问 | 练习项目答辩或检查理解程度 | `像项目主管一样问我 5 个问题` |
| 测试与审计 | 查看测试、数据流、风险点 | `审计这个项目的数据流和测试覆盖` |
| 前沿技术雷达 | 从项目中选技术点，调研最新项目、论文、benchmark，并判断是否值得借鉴 | `分析这个项目的技术点，找最新前沿启发` |
| GitHub 发布准备 | 发布前检查 README、license、敏感文件 | `先做 GitHub 发布前检查` |
| 求职表达 | 需要面试、简历、作品集整理时 | `整理成面试表达和简历可写点` |

## 自我进化

Intern Skill 会跟着你的学习过程一起调整。

它会记录项目地图、学习日志和阶段性反馈，用来判断你已经理解了什么、还卡在哪里、下一次应该讲到什么深度。这样它不会一直重复你已经知道的内容，也不会突然跳到你听不懂的层次。

你可以在学习一段时间后这样说：

```text
根据我这次学习的情况，帮我调整 Intern Skill 的讲解方式
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
