# Contributing to AI Code Helper

Thank you for your interest in contributing to this project! 🎉

## How to Contribute

### Adding New Templates

1. Fork this repository
2. Create a new branch for your contribution
   ```bash
   git checkout -b feature/add-new-template
   ```
3. Edit `app.js` to add your template in the appropriate category
4. Test your changes locally by opening `index.html` in a browser
5. Commit your changes with a descriptive message
   ```bash
   git commit -m "Add new template: [template name]"
   ```
6. Push to your fork
   ```bash
   git push origin feature/add-new-template
   ```
7. Open a Pull Request

### Template Format

Add a template in the appropriate section in `app.js`:

```javascript
yourCategory: [
    {
        title: 'Template Title / 模板标题',
        description: 'Description in English / 中文描述',
        content: `Template content here. / 这里是模板内容。

Use [placeholders] like this / 像这样使用[占位符]
- Option 1 / 选项1
- Option 2 / 选项2

The content will be copied to clipboard and sent to the AI assistant. / 内容将被复制到剪贴板并发送给AI助手。`
    }
]
```

**Important guidelines:**
- Include both English and Chinese in your content / 内容中包含英文和中文
- Use clear, descriptive titles / 使用清晰、描述性的标题
- Provide helpful descriptions / 提供有用的描述
- Include code examples where appropriate / 在适当的地方包含代码示例
- Ensure the content is beginner-friendly / 确保内容适合初学者
- Add comments for clarity / 添加注释以保持清晰

### Code Style

- Use 2 spaces for indentation / 使用2个空格缩进
- Follow existing code formatting / 遵循现有的代码格式
- Write clear, descriptive variable names / 编写清晰、描述性的变量名
- Add comments for complex logic / 为复杂的逻辑添加注释
- Ensure all templates are tested in the browser / 确保所有模板都在浏览器中测试

### Pull Request Guidelines

1. Make sure your PR is focused on a single feature or fix / 确保你的PR专注于单一功能或修复
2. Follow the template format / 遵循模板格式
3. Test your changes thoroughly / 彻底测试你的更改
4. Update the CHANGELOG.md if necessary / 如有必要，更新CHANGELOG.md
5. Add a clear, descriptive title and description / 添加清晰、描述性的标题和描述
6. Link related issues if applicable / 如果适用，链接相关的问题

## Translation

This project is bilingual (English and Chinese). If you can help improve translations:

1. Check existing templates for consistency / 检查现有模板的一致性
2. Suggest improvements or corrections / 建议改进或更正
3. Update translations in both English and Chinese sections / 更新英文和中文部分的翻译
4. Ensure technical terms are used consistently / 确保技术术语使用一致

## Reporting Bugs

If you find a bug:

1. Open an issue with a clear title / 使用清晰的标题打开问题
2. Describe the bug in detail / 详细描述bug
3. Include steps to reproduce / 包含重现步骤
4. Mention which browser/OS you're using / 提及你使用的浏览器/操作系统
5. Attach screenshots if applicable / 如果适用，附上截图

## Feature Requests

If you have an idea for a new feature:

1. Open an issue to discuss your idea / 打开问题讨论你的想法
2. Explain what the feature would do / 解释该功能将做什么
3. Describe how it would benefit users / 描述它如何为用户带来益处
4. Suggest an implementation approach if possible / 如可能，建议实现方法

## Questions

If you have questions about contributing:

1. Check the existing issues for similar questions / 查看现有的问题是否有类似问题
2. Open a new issue to ask / 打开新问题询问
3. Be specific about what you need help with / 具体说明你需要什么帮助

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

通过贡献，您同意您的贡献将根据MIT许可证进行许可。

## Thank You! 💜

Contributors make this project better for everyone. We appreciate your time and effort!
贡献者让这个项目变得更好。我们感谢您的时间和努力！
