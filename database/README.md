# Database Module

## 功能说明 / Functionality

此目录用于存储和管理应用程序的数据库相关配置和初始化代码。

This directory is used to store and manage database-related configuration and initialization code for the application.

## 使用指南 / Usage Guide

### 安装数据库驱动 / Install Database Drivers

在 `requirements.txt` 中添加数据库依赖：

Add database dependencies to `requirements.txt`:

```bash
# PostgreSQL driver
pip install psycopg2-binary

# MySQL driver
pip install mysqlclient

# SQLite (built-in)
# No installation needed
```

### 数据库配置 / Database Configuration

在 `app.py` 中配置数据库连接：

Configure database connection in `app.py`:

```python
import sqlite3

# SQLite example
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Execute queries
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
conn.commit()
```

### 数据模型 / Data Models

建议在此目录创建数据模型文件：

It is recommended to create data model files in this directory:

```python
# models.py
class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        # Initialize database tables
        pass

    def query(self, sql, params=None):
        # Execute query
        pass
```

## 支持的数据库 / Supported Databases

- **SQLite** - 默认选择，无需配置
- **PostgreSQL** - 企业级数据库
- **MySQL** - 通用关系型数据库

## 注意事项 / Important Notes

1. 数据库文件应包含在 `.gitignore` 中
2. 不要在代码中硬编码数据库凭据
3. 使用环境变量管理敏感信息
4. 定期备份数据库文件

## 更多信息 / More Information

参考项目主README文档获取更多详细信息。
