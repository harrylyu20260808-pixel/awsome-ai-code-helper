# Docs Module

## 功能说明 / Functionality

此目录用于存储应用程序的文档文件，包括API文档、部署指南、开发文档等。

This directory is used to store documentation files for the application, including API documentation, deployment guides, development documentation, etc.

## 文档类型 / Documentation Types

### 1. API文档 / API Documentation

#### API端点列表 / API Endpoints List

创建 `API.md` 文件：

Create `API.md` file:

```markdown
# API Documentation

## Endpoints

### POST /api/generate-code
Generate code based on requirements

**Request:**
```json
{
  "requirement": "Write a function",
  "language": "Python"
}
```

**Response:**
```json
{
  "code": "def example():\n    pass",
  "explanation": "Code explanation"
}
```

## Authentication
...
```

### 2. 部署指南 / Deployment Guide

创建 `DEPLOYMENT.md` 文件：

Create `DEPLOYMENT.md` file:

```markdown
# Deployment Guide

## Prerequisites
- Python 3.8+
- Node.js 14+ (for frontend)
- Nginx or Apache (optional)

## Production Setup

### 1. Environment Setup
```bash
cp .env.example .env
# Edit .env with production values
```

### 2. Database Setup
```bash
# Create database
python init_db.py
```

### 3. Configuration
Edit `config/prod_config.py` with production settings.

### 4. Build Frontend
```bash
npm run build
```

### 5. Start Server
```bash
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Monitoring
...
```

### 3. 开发指南 / Development Guide

创建 `DEVELOPMENT.md` 文件：

Create `DEVELOPMENT.md` file:

```markdown
# Development Guide

## Getting Started

### Clone Repository
```bash
git clone <repository-url>
cd ai-code-helper
```

### Setup Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running Development Server
```bash
python app.py
# Access at http://localhost:8000
```

## Development Workflow

1. Create feature branch
2. Make changes
3. Write tests
4. Run tests
5. Commit changes
6. Create pull request

## Code Style
...
```

### 4. 架构文档 / Architecture Documentation

创建 `ARCHITECTURE.md` 文件：

Create `ARCHITECTURE.md` file:

```markdown
# System Architecture

## Overview
This document describes the system architecture of AI Code Helper.

## Components

### Backend
- FastAPI application
- AI service integration
- Database layer

### Frontend
- Single Page Application
- Template engine
- Static assets

### Data Flow
...
```

### 5. 故障排查 / Troubleshooting

创建 `TROUBLESHOOTING.md` 文件：

Create `TROUBLESHOOTING.md` file:

```markdown
# Troubleshooting Guide

## Common Issues

### Issue: API Key not working
**Solution:** Check if API key is correctly configured in `.env` file.

### Issue: Database connection failed
**Solution:** Verify database URL and credentials.

### Issue: CORS errors
**Solution:** Configure CORS settings in `app.py`.

## Debug Mode
Enable debug mode by setting `DEBUG=True` in `.env`.
```

## 文档模板 / Documentation Templates

### 新增文档 / Add New Document

创建新的Markdown文档文件：

Create new Markdown documentation files:

```markdown
# Document Title

## Introduction
...

## Features
...

## Installation
...

## Usage
...

## Configuration
...

## API Reference
...

## Contributing
...

## License
```

### 更新文档 / Update Documentation

更新现有文档时，保持以下格式：

Update existing documentation while maintaining this format:

1. 使用清晰的标题层级（# ## ###）
2. 使用列表提高可读性
3. 提供代码示例
4. 包含故障排查信息
5. 保持文档最新

## 文档维护 / Documentation Maintenance

### 定期更新 / Regular Updates

1. 每次代码更改后更新相关文档
2. 添加新的功能说明
3. 修正错误信息
4. 更新示例代码

### 文档检查清单 / Documentation Checklist

- [ ] 所有链接有效
- [ ] 代码示例可运行
- [ ] 格式统一
- [ ] 内容准确
- [ ] 包含必要的截图或图表

## 工具推荐 / Recommended Tools

### 文档生成工具 / Documentation Generation Tools

- **Sphinx** - Python文档生成
- ** MkDocs** - 简单易用的文档工具
- **Docusaurus** - 现代化文档网站
- **Marp** - 幻灯片生成

### 文档编辑器 / Documentation Editors

- **VS Code** - 支持Markdown语法高亮
- **Typora** - 实时预览编辑器
- **Obsidian** - 双栏编辑

## 最佳实践 / Best Practices

1. 使用清晰的标题层级
2. 提供代码示例
3. 使用表格组织信息
4. 包含目录
5. 添加导航链接
6. 使用徽章标记状态
7. 保持语言简洁
8. 添加版权声明

## 更多信息 / More Information

参考项目主README文档获取更多详细信息。
