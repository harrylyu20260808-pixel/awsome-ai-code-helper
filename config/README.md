# Config Module

## 功能说明 / Functionality

此目录用于存储应用程序的配置文件、设置和环境变量。

This directory is used to store configuration files, settings, and environment variables for the application.

## 配置文件说明 / Configuration Files

### 环境变量文件 / Environment Variables

创建 `.env` 文件存储敏感信息：

Create `.env` file to store sensitive information:

```bash
# .env
ANTHROPIC_API_KEY=your-api-key-here
OPENAI_API_KEY=your-api-key-here
DATABASE_URL=sqlite:///database.db
DEBUG=False
```

### 配置文件模板 / Configuration File Templates

#### 默认配置 / Default Configuration

```python
# config/default_config.py
from pydantic import BaseSettings

class DefaultConfig(BaseSettings):
    # API配置
    api_provider: str = "claude"
    api_key: str = ""

    # 数据库配置
    database_url: str = "sqlite:///database.db"

    # 服务器配置
    host: str = "0.0.0.0"
    port: int = 8000

    # 功能开关
    enable_debug: bool = False
    enable_logging: bool = True

    class Config:
        env_file = ".env"
```

#### 开发环境配置 / Development Configuration

```python
# config/dev_config.py
from default_config import DefaultConfig

class DevConfig(DefaultConfig):
    DEBUG = True
    log_level = "DEBUG"
    host = "localhost"
```

#### 生产环境配置 / Production Configuration

```python
# config/prod_config.py
from default_config import DefaultConfig

class ProdConfig(DefaultConfig):
    DEBUG = False
    log_level = "INFO"
    enable_debug = False
```

## 配置加载 / Configuration Loading

在应用程序中使用配置：

Use configuration in the application:

```python
from config.default_config import settings

# Access configuration
print(f"API Provider: {settings.api_provider}")
print(f"Database URL: {settings.database_url}")
```

## 配置验证 / Configuration Validation

使用Pydantic进行配置验证：

Use Pydantic for configuration validation:

```python
from pydantic import BaseSettings, validator

class Config(BaseSettings):
    api_key: str

    @validator('api_key')
    def validate_api_key(cls, v):
        if not v:
            raise ValueError('API key cannot be empty')
        return v
```

## 安全建议 / Security Recommendations

1. 将敏感信息放在 `.env` 文件中，不提交到Git
2. 使用 `.gitignore` 排除 `.env` 文件
3. 不要在代码中硬编码密钥
4. 使用环境变量管理配置
5. 为生产环境创建单独的配置文件

## 配置文件示例 / Configuration File Examples

### .gitignore / 配置示例

```
# .gitignore
.env
.env.local
.env.production
*.pyc
__pycache__/
```

### 更新 requirements.txt / 更新依赖

```
pydantic>=2.0.0
python-dotenv>=1.0.0
```

## 更多信息 / More Information

参考项目主README文档获取更多详细信息。
