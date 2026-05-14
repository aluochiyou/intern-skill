# Project Intern Skill / 项目实习生 Skill

Project Intern 是一个帮助你学习开源项目的 Agent Skill。你给它一个 GitHub 仓库或本地项目，它会先帮你看清项目整体，再带你沿着核心代码链路一点点读懂。

它适合这些场景：

- 想学习一个开源项目，但不知道先看哪里。
- 想快速了解项目技术栈、入口文件和主要模块。
- 想让 AI 按你的水平解释代码，而不是直接抛出一堆专业术语。
- 想在需要时做环境检查、随机提问、测试审计、论文/相关项目启发或 GitHub 发布准备。

[English README](README.en.md)

## 定位

Project Intern 的目标不是替你一次性读完整个仓库，而是帮你建立一个清晰的学习入口：

1. 先判断项目是做什么的。
2. 找到主要入口和核心流程。
3. 按一个小模块、一个函数或一条调用链来学习。
4. 根据你的需求，再开启小白解释、随机提问、测试审计、论文启发、GitHub 发布等能力。

默认情况下，它会专注于“学习项目本身”。只有当你明确提出需要面试、简历、审计、发布或论文迁移时，它才会进入对应模式。

## 能做什么

- **下载与初步配置项目**：给 GitHub 链接后，克隆项目并生成启动报告。
- **识别项目结构**：整理技术栈、入口文件、测试目录、配置文件和文档位置。
- **生成项目地图**：输出 `docs/intern/PROJECT_MAP.md`，方便后续学习。
- **按主链路读代码**：从用户动作、CLI 命令、API 入口或核心函数开始讲。
- **小白友好解释**：先解释当前代码需要的概念，再进入源码。
- **环境体检**：检查 Python、Node、Docker、Git、GitHub CLI 等工具状态。
- **按需扩展**：在你需要时支持随机提问、测试审计、前沿论文/相关项目分析、GitHub 发布准备。

## 扩展模块

这些模块不会默认开启。你需要时，可以直接这样说：

- **小白模式**：适合刚接触项目或不熟悉技术栈时使用。  
  例：`我是小白，先解释这个项目需要的基础概念。`

- **环境配置**：用于下载 GitHub 项目、检查依赖、生成启动报告。  
  例：`帮我下载这个 GitHub 项目并检查怎么运行。`

- **测试与审计**：用于查看测试入口、数据流、日志、风险点和缺失检查。  
  例：`审计这个项目的数据流和测试覆盖。`

- **随机提问**：模拟项目主管或评审老师，随机挑重点考察你是否真正理解项目。  
  例：`像项目主管一样随机问我 5 个问题，先不要给答案。`

- **前沿启发**：用于根据论文、benchmark 或相关开源项目，分析当前项目可以借鉴什么。  
  例：`参考 SWE-agent，看看这个项目可以学习什么设计。`

- **GitHub 发布准备**：用于发布前检查 README、license、.gitignore、敏感文件和大文件。  
  例：`帮我发布这个项目到 GitHub，先做发布前检查。`

- **求职表达**：用于你明确想整理面试、简历、实习或作品集表达时。  
  例：`把这个模块整理成面试表达和简历可写点。`

## 自我进化怎么体现

Project Intern 会把重要学习过程沉淀到项目里的 `docs/intern/` 目录，例如项目地图、学习记录和评分记录。你可以在一次学习后让它复盘：

```text
根据这次学习效果，帮我评估 project-intern 哪里需要改进。
```

它会检查：

- 是否找到了项目主链路。
- 是否解释得符合你的水平。
- 是否证据充分。
- 是否一次讲得太多。
- 是否误开了不需要的扩展模块。
- 下一步是否清楚。

如果发现问题，它不会自动堆新功能，而是先提出一个最小修改建议。你确认后，再更新 skill。

## 安装

克隆本仓库后进入目录：

```bash
cd project-intern-skill
```

### 一键安装

如果你已经克隆了本仓库，可以直接运行：

```bash
bash scripts/install.sh --platform codex
```

发布到 GitHub 后，也可以提供类似下面的一键安装命令。把 `OWNER/REPO` 换成你的仓库地址：

```bash
PROJECT_INTERN_REPO_URL=https://github.com/OWNER/REPO.git \
  bash -c "$(curl -fsSL https://raw.githubusercontent.com/OWNER/REPO/main/scripts/install.sh)" -- --platform codex
```

安装到 Hermes Agent：

```bash
PROJECT_INTERN_REPO_URL=https://github.com/OWNER/REPO.git \
  bash -c "$(curl -fsSL https://raw.githubusercontent.com/OWNER/REPO/main/scripts/install.sh)" -- --platform hermes
```

安装到 OpenClaw / miniOpenClaw：

```bash
PROJECT_INTERN_REPO_URL=https://github.com/OWNER/REPO.git \
  bash -c "$(curl -fsSL https://raw.githubusercontent.com/OWNER/REPO/main/scripts/install.sh)" -- --platform openclaw --openclaw-project /path/to/miniOpenClaw-main
```

### Codex

```bash
python scripts/install.py --platform codex
```

安装到：

```text
~/.codex/skills/project-intern
```

### Claude Code

```bash
python scripts/install.py --platform claude
```

安装到：

```text
~/.claude/skills/project-intern
```

### Hermes Agent

```bash
python scripts/install.py --platform hermes
```

安装到：

```text
$HERMES_HOME/skills/project-intern
```

如果没有设置 `HERMES_HOME`，默认是：

```text
~/.hermes/skills/project-intern
```

如果 Hermes 会话已经在运行，安装后在 Hermes 中执行：

```text
/reload-skills
```

### OpenClaw / miniOpenClaw

传入项目根目录或 `backend` 目录：

```bash
python scripts/install.py --platform openclaw --openclaw-project /path/to/miniOpenClaw-main
```

安装到：

```text
/path/to/miniOpenClaw-main/backend/skills/project-intern
```

### 安装到全部平台

```bash
python scripts/install.py --platform all --openclaw-project /path/to/miniOpenClaw-main
```

如果目标目录已经存在，使用：

```bash
python scripts/install.py --platform codex --force
```

## 使用方法

学习 GitHub 项目：

```text
用 project-intern 学习这个项目：https://github.com/NousResearch/hermes-agent
```

学习本地项目：

```text
用 project-intern 学习当前项目，先帮我建立项目地图
```

小白模式：

```text
我是小白，先解释这个项目里的 tool call、memory、skill 是什么
```

继续学习某个模块：

```text
继续学习 AIAgent.run_conversation 主循环，只讲这一段
```

环境检查：

```text
检查这个项目的运行环境还缺什么
```

测试与审计：

```text
审计这个项目的数据流和测试覆盖
```

随机提问：

```text
像项目主管一样随机问我 5 个问题，先不要给答案
```

前沿论文或相关项目启发：

```text
参考 SWE-agent，看看这个项目可以学习什么设计
```

GitHub 发布准备：

```text
帮我发布这个项目到 GitHub，先做发布前检查
```

## 配置与检查

发布或分发前可以运行：

```bash
python scripts/check_package.py
```

它会检查 skill 文件、安装脚本和 Python 脚本是否可用。

## 目录结构

```text
project-intern-skill/
├── README.md
├── README.en.md
├── scripts/
│   ├── install.py
│   └── check_package.py
└── skills/
    └── project-intern/
        ├── SKILL.md
        ├── references/
        └── scripts/
```

## License

MIT
