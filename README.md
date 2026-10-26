# Python Learning Journal

一个为期两周的 Python 学习与输出仓库：从基础语法到 FastAPI Web 后端、httpx + BeautifulSoup 爬虫，并用掘金/CSDN 笔记记录真实踩坑过程。

## 目标

- 两周内完成一个可运行的小项目：LinkVault 链接采集与收藏 API
- 每天留下可运行的代码和一次 Git 提交
- 每周至少发布 2 篇有代码、有问题、有复盘的技术笔记
- 用 README、测试和 Demo 证明项目可运行，而不是只堆教程代码

> 两周的目标是“能独立做出小型项目”，不是“达到生产级后端工程师”。

## 技术栈

| 方向 | 选择 |
| --- | --- |
| 语言 | Python 3.12+ |
| Web | FastAPI、Uvicorn、Pydantic |
| 数据库 | SQLite、SQLAlchemy 2.x |
| 爬虫 | httpx、BeautifulSoup4 |
| 测试 | pytest、FastAPI TestClient |
| 部署 | Docker、Render/Railway（可选） |

## 仓库结构

```text
.
├── README.md
├── PROGRESS.md              # 14 天进度与验收
├── resources.md             # 官方文档和练习站
├── notes/                   # 学习笔记草稿与发布索引
├── projects/
│   └── link-vault/          # 两周主项目
└── .gitignore
```

## 14 天路线

| 阶段 | 时间 | 重点 | 产出 |
| --- | --- | --- | --- |
| 基础 | Day 1-3 | 语法、函数、模块、Git | 命令行小工具 |
| 爬虫 | Day 4-7 | HTTP、httpx、BeautifulSoup、测试 | 100 条数据爬虫 |
| 后端 | Day 8-12 | FastAPI、SQLite、认证、整合 | LinkVault API |
| 收尾 | Day 13-14 | Docker、部署、README、复盘 | Demo + 文章 |

详细任务见 [PROGRESS.md](PROGRESS.md)。

## 笔记发布

- 草稿放在 `notes/`，文件名使用 `YYYY-MM-DD-topic.md`
- 发布平台：掘金为主，CSDN 同步
- 每篇笔记必须包含：问题、代码、报错、解决过程、结论
- 发布后在 [notes/README.md](notes/README.md) 登记链接

## 每日节奏

- 20 分钟：读官方文档
- 90 分钟：写代码并运行
- 30 分钟：测试、提交 Git、写笔记
- 10 分钟：口述今天学会了什么

## 项目验收

- 爬虫能抓取 100 条记录，支持分页、去重、限速、超时和重试
- API 支持 CRUD、分页、搜索和统一错误响应
- 至少有解析器和接口测试
- README 能让别人按步骤跑起来
- Demo 有截图或 GIF

## 说明

本项目只用于学习和技术记录。爬虫示例必须遵守目标站点的 robots.txt、服务条款和访问频率限制，不抓取个人隐私数据，不绕过验证码或登录。

