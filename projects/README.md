# 项目

两周只做一个主项目：LinkVault。

## 为什么只做一个

- 一个完整项目比五个半成品更能证明能力
- 后端和爬虫可以在同一个项目里串起来
- README、测试、提交记录都能围绕同一条主线积累

## 目录约定

```text
projects/
└── link-vault/
    ├── README.md
    ├── app/          # FastAPI 应用
    ├── crawler/      # 抓取与解析
    ├── tests/        # pytest
    └── ...
```

## 项目推进顺序

1. 爬虫模块：给定 URL，返回标题和描述
2. 数据库：保存链接、状态、错误和时间
3. API：提交、查询、搜索、分页
4. 整合：提交 URL 后触发抓取
5. 测试：解析器和接口
6. 展示：Docker、部署、README、Demo

