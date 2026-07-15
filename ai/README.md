# AI Module

## 功能说明 / Functionality

此目录用于存储AI相关的模块、API集成和服务，包括多个AI平台的适配器。

This directory is used to store AI-related modules, API integrations, and services, including adapters for multiple AI platforms.

## 支持的AI平台 / Supported AI Platforms

### 1. Claude API / Claude API

Anthropic官方API服务：

Anthropic's official API service:

```python
# ai/claude_service.py
import anthropic

class ClaudeService:
    """Claude API服务类

    Claude API service class
    """

    def __init__(self, api_key: str):
        """初始化Claude服务

        Initialize Claude service

        Args:
            api_key: Anthropic API密钥
            api_key: Anthropic API key
        """
        self.client = anthropic.Anthropic(api_key=api_key)

    async def generate_code(self, prompt: str, language: str = "Python") -> str:
        """生成代码

        Generate code

        Args:
            prompt: 用户需求
            prompt: User requirement
            language: 编程语言
            language: Programming language

        Returns:
            生成的代码
            Generated code
        """
        system_prompt = f"""你是一个专业的编程助手。请根据用户需求生成{language}代码。
You are a professional programming assistant. Generate {language} code based on user requirements."""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        return response.content[0].text

    async def debug_code(self, error: str, code: str) -> dict:
        """调试代码

        Debug code

        Args:
            error: 错误信息
            error: Error message
            code: 出错的代码
            code: Error code

        Returns:
            包含修复建议的字典
            Dictionary containing fix suggestions
        """
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[
                {"role": "system", "content": "你是一个代码调试专家。分析错误并提供修复方案。"},
                {"role": "user", "content": f"错误信息: {error}\n\n代码:\n{code}"}
            ]
        )

        return {
            "explanation": response.content[0].text,
            "fixed_code": response.content[0].text  # 实际应用中需要解析
        }
```

### 2. OpenAI API / OpenAI API

OpenAI的ChatGPT API服务：

OpenAI's ChatGPT API service:

```python
# ai/openai_service.py
import openai

class OpenAIService:
    """OpenAI API服务类

    OpenAI API service class
    """

    def __init__(self, api_key: str):
        """初始化OpenAI服务

        Initialize OpenAI service

        Args:
            api_key: OpenAI API密钥
            api_key: OpenAI API key
        """
        self.client = openai.AsyncOpenAI(api_key=api_key)

    async def generate_code(self, prompt: str, language: str = "Python") -> str:
        """生成代码

        Generate code

        Args:
            prompt: 用户需求
            prompt: User requirement
            language: 编程语言
            language: Programming language

        Returns:
            生成的代码
            Generated code
        """
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"你是一个专业的编程助手。请生成{language}代码。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2048,
            temperature=0.7
        )

        return response.choices[0].message.content

    async def debug_code(self, error: str, code: str) -> dict:
        """调试代码

        Debug code

        Args:
            error: 错误信息
            error: Error message
            code: 出错的代码
            code: Error code

        Returns:
            包含修复建议的字典
            Dictionary containing fix suggestions
        """
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个代码调试专家。"},
                {"role": "user", "content": f"错误: {error}\n代码: {code}"}
            ],
            max_tokens=2048
        )

        return {
            "explanation": response.choices[0].message.content,
            "fixed_code": response.choices[0].message.content
        }
```

### 3. Hermes API / Hermes API

## 服务统一接口 / Unified Service Interface

创建统一的服务接口：

Create unified service interface:

```python
# ai/service_factory.py
from ai.claude_service import ClaudeService
from ai.openai_service import OpenAIService

class AIServiceFactory:
    """AI服务工厂类

    AI service factory class
    """

    @staticmethod
    def create_service(provider: str, api_key: str):
        """创建AI服务实例

        Create AI service instance

        Args:
            provider: AI提供商 (claude/openai/hermes)
            provider: AI provider
            api_key: API密钥
            api_key: API key

        Returns:
            AI服务实例
            AI service instance

        Raises:
            ValueError: 不支持的AI提供商
            ValueError: Unsupported AI provider
        """
        if provider == "claude":
            return ClaudeService(api_key)
        elif provider == "openai":
            return OpenAIService(api_key)
        elif provider == "hermes":
            raise NotImplementedError("Hermes API integration not yet implemented")
        else:
            raise ValueError(f"Unsupported AI provider: {provider}")
```

## 使用示例 / Usage Examples

### 基础使用 / Basic Usage

```python
from ai.service_factory import AIServiceFactory
from ai.claude_service import ClaudeService

# 创建Claude服务实例
api_key = "your-api-key"
claude_service = AIServiceFactory.create_service("claude", api_key)

# 生成代码
code = await claude_service.generate_code("写一个Python函数", "Python")

# 调试代码
result = await claude_service.debug_code("NameError", "print(x)")
```

### 配置管理 / Configuration Management

```python
# ai/config.py
from ai.service_factory import AIServiceFactory

def get_ai_service():
    """获取配置的AI服务

    Get configured AI service
    """
    provider = os.getenv("AI_PROVIDER", "claude")
    api_key = os.getenv(f"{provider.upper()}_API_KEY")

    if not api_key:
        raise ValueError("API key not configured")

    return AIServiceFactory.create_service(provider, api_key)
```

## 错误处理 / Error Handling

### 错误类定义 / Error Class Definition

```python
# ai/errors.py

class AIServiceError(Exception):
    """AI服务错误基类

    Base class for AI service errors
    """
    pass

class APIKeyError(AIServiceError):
    """API密钥错误

    API key error
    """
    pass

class APIRateLimitError(AIServiceError):
    """API速率限制错误

    API rate limit error
    """
    pass

class ServiceUnavailableError(AIServiceError):
    """服务不可用错误

    Service unavailable error
    """
    pass
```

## 最佳实践 / Best Practices

1. 将API密钥存储在环境变量中
2. 使用统一的错误处理机制
3. 实现重试逻辑处理速率限制
4. 添加请求超时控制
5. 记录API调用日志
6. 考虑添加缓存机制

## 安全建议 / Security Recommendations

1. 不要在代码中硬编码API密钥
2. 使用环境变量或配置文件管理密钥
3. 定期轮换API密钥
4. 实现API密钥权限控制
5. 记录API调用日志用于审计

## 更多信息 / More Information

参考项目主README文档获取更多详细信息。
