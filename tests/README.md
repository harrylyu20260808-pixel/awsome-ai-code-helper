# Tests Module

## 功能说明 / Functionality

此目录用于存储应用程序的测试文件，包括单元测试、集成测试和端到端测试。

This directory is used to store test files for the application, including unit tests, integration tests, and end-to-end tests.

## 测试框架 / Testing Framework

### 安装测试框架 / Install Testing Framework

```bash
pip install pytest pytest-asyncio pytest-cov
```

### 基础配置 / Basic Configuration

创建 `pytest.ini` 文件：

Create `pytest.ini` file:

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --cov=.
    --cov-report=html
    --cov-report=term-missing
```

## 测试文件结构 / Test File Structure

### 单元测试示例 / Unit Test Example

```python
# tests/test_utils.py
import pytest
from core.utils import validate_input

def test_validate_input_valid():
    """Test valid input validation"""
    assert validate_input("test") == True

def test_validate_input_empty():
    """Test empty input validation"""
    assert validate_input("") == False

def test_validate_input_special_chars():
    """Test special characters validation"""
    assert validate_input("test@123") == True
```

### 集成测试示例 / Integration Test Example

```python
# tests/test_integration.py
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_generate_code_endpoint():
    """Test code generation API endpoint"""
    response = client.post(
        "/api/generate-code",
        json={
            "requirement": "Write a Python function",
            "language": "Python"
        }
    )
    assert response.status_code == 200
    assert "code" in response.json()

def test_debug_code_endpoint():
    """Test code debugging API endpoint"""
    response = client.post(
        "/api/debug-code",
        json={
            "error": "NameError",
            "code": "print(x)"
        }
    )
    assert response.status_code == 200
```

### API测试示例 / API Test Example

```python
# tests/test_api.py
import pytest
from app import call_ai

@pytest.mark.asyncio
async def test_call_ai():
    """Test AI call function"""
    # 注意：需要配置真实的API密钥
    result = await call_ai("Test prompt")
    assert isinstance(result, str)
    assert len(result) > 0
```

## 测试覆盖 / Test Coverage

### 运行测试 / Run Tests

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_utils.py

# 运行特定测试
pytest tests/test_utils.py::test_validate_input_valid

# 显示详细输出
pytest -v

# 显示覆盖率报告
pytest --cov=.
```

### 测试覆盖率要求 / Test Coverage Requirements

建议的测试覆盖率目标：

Suggested test coverage targets:

- 核心功能：> 80%
- 工具函数：> 90%
- API端点：> 70%
- 边界情况：100%

## Mock测试 / Mock Testing

### 使用 pytest-mock / Using pytest-mock

```python
from unittest.mock import Mock, patch

def test_with_mock():
    """Test with mocked dependencies"""
    with patch('core.ai_service.AIService') as mock_ai:
        mock_ai.return_value.generate_code.return_value = "Mocked code"

        result = mock_ai.return_value.generate_code("test")
        assert result == "Mocked code"
```

## 测试数据 / Test Data

### 测试数据文件 / Test Data Files

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_code():
    """Sample code for testing"""
    return """
def example_function():
    return 42
"""

@pytest.fixture
def sample_error():
    """Sample error for testing"""
    return "NameError: name 'x' is not defined"
```

## 最佳实践 / Best Practices

1. 每个测试文件命名以 `test_` 开头
2. 每个测试函数命名清晰描述测试内容
3. 测试应该是独立的，不依赖执行顺序
4. 使用断言确保测试通过
5. 添加测试文档说明测试目的
6. 定期运行测试确保代码质量

## 测试类型 / Test Types

### 单元测试 / Unit Tests
- 测试单个函数或类的行为
- 不依赖外部系统
- 快速执行

### 集成测试 / Integration Tests
- 测试多个模块的交互
- 测试API端点
- 验证完整功能流程

### 端到端测试 / End-to-End Tests
- 测试完整的应用程序流程
- 模拟用户操作
- 验证真实场景

## 更多信息 / More Information

参考项目主README文档获取更多详细信息。
