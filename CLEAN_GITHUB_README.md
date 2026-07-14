# AI Code Helper - 开源项目

一个面向编程新手的AI编程助手，包含代码生成、调试、解释功能。

## 📋 项目简介

这个项目提供了：

- **代码生成**：简单的表单输入，AI自动生成代码
- **自动调试**：粘贴报错信息，AI自动修复
- **代码解释**：逐行解释代码，新手友好
- **提示词模板库**：60+预构建模板，支持自定义

## 🚀 快速开始

### 环境要求

- Python 3.8+
- pip包管理器
- 现代浏览器

### 安装步骤

```bash
# 1. 克隆项目
git clone https://github.com/yourusername/ai-code-helper.git
cd ai-code-helper

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动服务器
python app.py

# 4. 访问应用
# 浏览器打开 http://localhost:8000
```

### 提示词模板库

```bash
# 直接在浏览器中打开
open english-prompt-library/index.html

# 或使用本地服务器
python3 -m http.server 8001 -d english-prompt-library
```

## 📁 项目结构

```
ai-code-helper/
├── app.py                    # FastAPI后端主程序
├── utils.py                  # 核心工具函数
├── requirements.txt          # Python依赖
├── templates/                # HTML模板
│   ├── index.html            # 首页
│   ├── debug.html            # 调试页
│   └── explain.html          # 解释页
├── static/                   # 静态资源
│   ├── style.css             # 样式文件
│   └── app.js                # JavaScript逻辑
├── english-prompt-library/   # 提示词模板库
│   ├── index.html            # 模板库主页
│   ├── style.css             # 样式文件
│   └── app.js                # 逻辑文件
├── data/                     # 数据和教程
│   ├── python_basics_tutorial.py
│   ├── javascript_tutorial.js
│   ├── ml_tutorial.py
│   ├── excel_processing_tutorial.py
│   ├── database_tutorial.py
│   ├── web_framework_tutorial.py
│   ├── web_scraping_example.py
│   └── comprehensive_guide.md
├── examples/                 # 示例项目
│   ├── portfolio_manager.py
│   ├── stock_analyzer.py
│   ├── weather_app.py
│   └── calculator_app.py
├── modules/                  # 模块化代码
│   └── calculator_app.py
├── apps/                     # 应用示例
│   ├── portfolio_manager.py
│   ├── stock_analyzer.py
│   └── weather_app.py
├── docs/                     # 文档
│   ├── API.md
│   ├── DEPLOYMENT.md
│   └── CONTRIBUTING.md
├── tests/                    # 测试
├── CLAUDE.md                 # Claude Code文档
├── README.md                 # 本文件
├── PROJECT_STATUS.md         # 项目状态
└── LICENSE                   # MIT许可证
```

## 🎯 核心功能

### 1. 代码生成

```
需求 → AI生成代码 → 查看解释 → 复制/下载
```

### 2. 自动调试

```
报错信息 + 出错代码 → AI分析并修复 → 复制/下载
```

### 3. 代码解释

```
输入代码 → 逐行解释 → 理解每一行
```

## 🔧 AI集成

项目预留了AI集成接口，支持：

- **Claude API**
- **OpenAI API**
- **Hermes API**
- **Mock模式**（演示用）

### 使用Claude API

编辑 `app.py` 中的 `call_ai()` 函数：

```python
import anthropic
import os

async def call_ai(prompt: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
```

设置环境变量：

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## 📚 教程资源

项目包含完整的学习资源：

- [Python基础教程](data/python_basics_tutorial.py)
- [JavaScript教程](data/javascript_tutorial.js)
- [机器学习教程](data/ml_tutorial.py)
- [Excel数据处理教程](data/excel_processing_tutorial.py)
- [数据库教程](data/database_tutorial.py)
- [Web框架教程](data/web_framework_tutorial.py)
- [全栈开发指南](data/comprehensive_guide.md)

## 🧪 测试

```bash
# 运行测试
python3 test_api.py

# 或使用pytest
pip install pytest
pytest
```

## 📊 性能

- **响应时间**：< 5秒（AI调用）
- **页面加载**：< 1秒
- **并发支持**：10+ 用户

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- 遵循 PEP 8 (Python)
- 使用类型注解
- 添加文档字符串
- 编写单元测试

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- FastAPI - 现代Web框架
- Jinja2 - 模板引擎
- Claude API - AI服务
- 所有贡献者

## 📮 联系方式

- 项目主页：https://github.com/yourusername/ai-code-helper
- 问题反馈：https://github.com/yourusername/ai-code-helper/issues
- 邮箱：your-email@example.com

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给它一个Star！⭐**

Made with ❤️

</div>
