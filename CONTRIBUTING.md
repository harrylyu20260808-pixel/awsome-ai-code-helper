# 贡献指南

欢迎贡献代码！以下是贡献项目的步骤。

## 如何贡献

### 1. Fork项目

点击页面右上角的 "Fork" 按钮来创建你自己的分支。

### 2. 创建新分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-bug-fix
```

### 3. 进行修改

- 遵循现有代码的风格和结构
- 添加必要的注释和文档
- 确保代码可以正常运行

### 4. 测试修改

在提交前，确保：
- 运行 `python3 test_api.py` 测试API
- 测试所有功能是否正常工作
- 检查代码格式（使用black和isort）

### 5. 提交更改

```bash
git add .
git commit -m "feat: add your feature"
# 或
git commit -m "fix: fix your bug"
```

### 6. 推送到分支

```bash
git push origin feature/your-feature-name
```

### 7. 创建Pull Request

在GitHub上创建Pull Request，描述你的更改。

## 代码规范

### Python代码

- 遵循 PEP 8 规范
- 使用 type hints（类型提示）
- 添加函数和类的文档字符串
- 使用有意义的变量和函数名

示例：
```python
def generate_code_prompt(requirement: str, language: str) -> str:
    """
    生成AI调用的prompt

    Args:
        requirement: 用户需求
        language: 编程语言

    Returns:
        生成的prompt
    """
    # 你的代码
    return prompt
```

### 前端代码

- 遵循现有的代码风格
- 添加适当的注释
- 使用有意义的变量名
- 确保代码可读性

## 文档规范

所有公共函数、类和模块都需要文档字符串：
- 使用简洁明了的语言
- 说明函数的用途、参数和返回值
- 包含示例（如果适用）

## 测试规范

- 新功能必须包含测试
- 测试要覆盖主要功能
- 测试要容易理解和运行

## 开发工作流

1. 创建feature分支
2. 进行开发
3. 测试你的更改
4. 更新文档
5. 提交更改
6. 创建Pull Request

## 问题报告

如果你发现bug或有新功能建议：

1. 搜索现有issues，确保没有重复
2. 创建新的issue，包含：
   - 问题描述
   - 复现步骤
   - 预期结果
   - 实际结果
   - 环境信息

## 行为准则

- 尊重所有贡献者
- 保持建设性反馈
- 避免人身攻击
- 关注对项目的改进

## 许可证

通过贡献代码，你同意你的贡献将按照MIT许可证发布。

## 感谢

感谢所有贡献者！
