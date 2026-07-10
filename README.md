# awsome-ai-code-helper

这是一个为 AI 编程助手准备的高质量 prompt 库（Prompts Library），旨在帮助开发者快速找到并复用适合的提示词（prompts），以提升代码生成、重构、调试与文档编写效率。

This is a high-quality prompts library for AI coding assistants. It helps developers quickly find and reuse prompts suitable for code generation, refactoring, debugging, and documentation.

由 Claudecode 自动生成并经人工审核（Claudecode-generated, human-reviewed）。

由 Claudecode 自动生成，随后由人工审核团队对示例进行校验和改进，确保可用性与准确性。

主要功能 / Features
- 按语言与场景组织的 prompt（例如：Python、JavaScript、单元测试、重构、性能优化、错误定位等）
- 可直接复制粘贴的 prompt 模板与使用说明
- 示例输入/输出（如果适用）与最佳实践建议
- 欢迎社区贡献：新增 prompt、改进模板、提交示例

- Prompts organized by language and scenario (e.g., Python, JavaScript, testing, refactoring, performance tuning, bug localization).
- Copy-paste ready prompt templates and usage notes.
- Example I/O (where applicable) and best-practice recommendations.
- Community contributions are welcome: add prompts, improve templates, submit examples.

仓库结构建议 / Suggested repository structure
- /prompts/            —— 按语言/场景组织的 prompt 文件或子目录
  - /prompts/python/
  - /prompts/javascript/
  - /prompts/devops/
  - /prompts/testing/
- /examples/           —— 使用示例、输入/输出对比
- /templates/          —— 通用 prompt 模板与最佳实践
- README.md
- CONTRIBUTING.md      —— 贡献与人工审核流程（本仓库已包含）
- LICENSE

Quick start / 快速开始
1. 浏览 /prompts/ 下的分类文件或子目录，查找与你的任务匹配的 prompt。
2. 复制所需 prompt 并粘贴到你的 LLM（例如 ChatGPT、Copilot、Claude）对话框或工具中。
3. 根据项目背景或上下文对 prompt 进行必要调整（添加代码片段、目标要求、约束条款等）。
4. 评估生成结果并按照需要迭代 prompt。所有要合并到主分支的内容需通过人工审核。

Generation & Review / 生成与人工审核
- 本项目内大部分 prompt 由 Claudecode 自动生成（Claudecode-generated）。
- 所有准备合并到主分支的 prompt，均要求人工审核（包括但不限于格式校验、可执行示例、预期输出验证）。
- Auto-generated prompts may contain issues; human reviewers validate and improve prompts before merging to main.

示例 Prompt 模板 / Example prompt templates
- 生成函数实现 / Generate function implementation
  "你是一个熟练的 [语言] 开发者。请根据下面的说明实现函数，并返回仅包含代码的完整实现（不带解释）。需求：{功能描述}。注意：{性能/安全/兼容性要求}。"

- 编写单元测试 / Write unit tests
  "为下面的函数编写单元测试，使用 [测试框架]，覆盖正常路径与边界条件。只返回测试代码。函数代码：{插入代码}。"

- 定位 BUG / Debugging
  "下面的代码在 {描述错误行为}。请指出可能的根因并给出修复建议，给出修改后的代码片段。代码：{插入代码}。"

贡献（简要）/ Contributing (brief)
- 欢迎贡献新的 prompt、改进已有模板或提交示例。请参阅 CONTRIBUTING.md 获得详细流程。
- Contributions should follow the CONTRIBUTING.md process and will be manually reviewed before merge.

许可证 / License
- 请参阅仓库中的 LICENSE 文件以获取许可信息。

致谢 / Acknowledgements
- Claudecode（自动生成）
- 人工审核团队（示例校验与维护）

联系方式 / Contact
- 有问题、建议或愿意参与审核，请打开 issue 或发起 PR。

---

（注：本 README 由 GitHub Copilot Chat Assistant 协助生成。项目中的 prompt 内容为 Claudecode 生成并经过人工审核。）