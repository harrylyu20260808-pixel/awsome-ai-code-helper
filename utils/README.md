# Utils Module

## 功能说明 / Functionality

此目录包含应用程序的工具函数和辅助类，用于提高代码复用性和可维护性。

This directory contains utility functions and helper classes for the application, improving code reusability and maintainability.

## 工具函数列表 / Utility Functions

### 1. 字符串处理 / String Processing

#### 格式化字符串 / Formatting Strings

```python
# utils/string_utils.py

def format_code(code: str) -> str:
    """格式化代码显示
    Format code display

    Args:
        code: 原始代码字符串
        code: Original code string

    Returns:
        格式化后的代码
        Formatted code
    """
    return code.strip()

def truncate_text(text: str, max_length: int = 100) -> str:
    """截断文本
    Truncate text

    Args:
        text: 原始文本
        text: Original text
        max_length: 最大长度
        max_length: Maximum length

    Returns:
        截断后的文本
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
```

### 2. 文件处理 / File Processing

#### 文件读写 / File Read/Write

```python
# utils/file_utils.py

def read_file(file_path: str) -> str:
    """读取文件内容
    Read file content

    Args:
        file_path: 文件路径
        file_path: File path

    Returns:
        文件内容
        File content
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path: str, content: str) -> None:
    """写入文件内容
    Write file content

    Args:
        file_path: 文件路径
        file_path: File path
        content: 文件内容
        content: File content
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
```

### 3. 数据验证 / Data Validation

#### 输入验证 / Input Validation

```python
# utils/validation_utils.py

def validate_email(email: str) -> bool:
    """验证邮箱格式
    Validate email format

    Args:
        email: 邮箱地址
        email: Email address

    Returns:
        是否有效
        Is valid
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_code_format(code: str, language: str) -> bool:
    """验证代码格式
    Validate code format

    Args:
        code: 代码内容
        code: Code content
        language: 编程语言
        language: Programming language

    Returns:
        是否有效
        Is valid
    """
    if language == "Python":
        return "def " in code or "class " in code
    elif language == "JavaScript":
        return "function" in code or "=" in code
    return True
```

### 4. 响应处理 / Response Handling

#### 格式化响应 / Format Response

```python
# utils/response_utils.py

def format_api_response(success: bool, message: str, data: dict = None) -> dict:
    """格式化API响应
    Format API response

    Args:
        success: 是否成功
        success: Is success
        message: 消息内容
        message: Message content
        data: 响应数据
        data: Response data

    Returns:
        格式化的响应字典
        Formatted response dictionary
    """
    response = {
        "success": success,
        "message": message
    }
    if data is not None:
        response["data"] = data
    return response
```

### 5. 缓存工具 / Cache Utilities

#### 简单缓存 / Simple Cache

```python
# utils/cache_utils.py

class SimpleCache:
    """简单缓存实现
    Simple cache implementation
    """

    def __init__(self, max_size: int = 100):
        """初始化缓存
        Initialize cache

        Args:
            max_size: 最大缓存大小
            max_size: Maximum cache size
        """
        self.cache = {}
        self.max_size = max_size

    def get(self, key: str):
        """获取缓存值
        Get cache value

        Args:
            key: 缓存键
            key: Cache key

        Returns:
            缓存值
            Cache value
        """
        return self.cache.get(key)

    def set(self, key: str, value) -> None:
        """设置缓存值
        Set cache value

        Args:
            key: 缓存键
            key: Cache key
            value: 缓存值
            value: Cache value
        """
        if len(self.cache) >= self.max_size:
            # 简单的LRU策略：删除第一个键
            self.cache.popitem()
        self.cache[key] = value

    def clear(self) -> None:
        """清空缓存
        Clear cache
        """
        self.cache.clear()
```

## 使用示例 / Usage Examples

### 在应用中使用 / Use in Application

```python
from utils import string_utils, file_utils

# 字符串处理
formatted_code = string_utils.format_code(code)
short_text = string_utils.truncate_text(long_text, 50)

# 文件处理
content = file_utils.read_file('config.json')
file_utils.write_file('output.txt', content)
```

## 性能优化 / Performance Optimization

1. 避免在循环中重复计算
2. 使用缓存存储频繁访问的数据
3. 合理使用生成器处理大数据
4. 避免不必要的对象创建

## 扩展指南 / Extension Guide

添加新的工具函数：

Add new utility functions:

```python
# utils/new_utils.py

def new_function(param1, param2):
    """新函数说明
    New function description

    Args:
        param1: 参数1说明
        param1: Parameter 1 description
        param2: 参数2说明
        param2: Parameter 2 description

    Returns:
        返回值说明
        Return value description
    """
    # 实现代码
    pass
```

## 更多信息 / More Information

参考项目主README文档获取更多详细信息。
