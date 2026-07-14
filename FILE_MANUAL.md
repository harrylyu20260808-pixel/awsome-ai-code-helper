# AI Code Helper - 完整操作指南

本文档详细说明项目中每个文件的功能、用途和使用方法。

---

## 📂 项目根目录文件说明

### 🎯 核心文件

#### `app.py` (480行)
**功能**: FastAPI主应用程序

**作用**:
- 提供Web服务器，运行在 `http://localhost:8000`
- 实现三大核心功能：代码生成、自动调试、代码解释
- 处理前端页面的路由和API请求
- 提供3个API端点供其他程序调用

**如何使用**:
```bash
python3 app.py
```

**访问地址**:
- 主应用: http://localhost:8000
- 代码生成: http://localhost:8000/
- 调试功能: http://localhost:8000/debug
- 代码解释: http://localhost:8000/explain

**API端点**:
- `POST /api/generate-code` - 生成代码
- `POST /api/debug-code` - 修复代码
- `POST /api/explain-line` - 解释代码行

**示例**:
```bash
curl -X POST http://localhost:8000/api/generate-code \
  -H "Content-Type: application/json" \
  -d '{"requirement": "写一个计算器", "language": "Python"}'
```

---

#### `utils.py` (180行)
**功能**: 工具函数库

**作用**:
- 提供代码生成、错误分析、代码解释的核心逻辑
- 为app.py提供支持函数
- 提供代码语法检查功能

**主要函数**:

1. **`generate_code_prompt(requirement, language)`**
   - 生成AI调用的prompt
   - 支持的语言：Python, JavaScript, Java, C++
   - 参数：
     - `requirement`: 用户需求描述
     - `language`: 编程语言
   - 返回：格式化的prompt字符串

2. **`analyze_error(error_message)`**
   - 分析错误信息，返回通俗易懂的解释
   - 支持的错误类型：
     - SyntaxError (语法错误)
     - NameError (变量名错误)
     - TypeError (类型错误)
     - IndexError (索引错误)
     - ValueError (值错误)
     - KeyError (键错误)
     - AttributeError (属性错误)
   - 返回：新手友好的错误解释

3. **`explain_code_line(code, line_number)`**
   - 逐行解释代码
   - 参数：
     - `code`: 完整代码
     - `line_number`: 要解释的行号（从1开始）
   - 返回：该行的详细解释

4. **`check_syntax(code, language)`**
   - 检查代码语法（简单模拟）
   - 检查未闭合的括号、未闭合的引号
   - 返回：验证结果和错误列表

**使用示例**:
```python
from utils import generate_code_prompt, analyze_error, explain_code_line

# 生成prompt
prompt = generate_code_prompt("写一个函数", "Python")
print(prompt)

# 分析错误
error = analyze_error("NameError: x is not defined")
print(error)

# 解释代码
explanation = explain_code_line("def hello():\n    print('Hello')", 1)
print(explanation)
```

---

#### `test_manual.py` (103行)
**功能**: 手动测试脚本

**作用**:
- 验证所有核心功能是否正常工作
- 检查文件结构完整性
- 测试工具函数

**如何使用**:
```bash
python3 test_manual.py
```

**测试内容**:
1. ✅ 导入模块测试
2. ✅ 工具函数测试（prompt生成、错误分析、代码解释）
3. ✅ 文件结构检查
4. ✅ 文档完整性检查

**输出示例**:
```
============================================================
Testing AI Code Helper Components
============================================================

📍 Test 1: Import Modules
✓ All utility functions imported successfully

📍 Test 2: Test Utility Functions
✓ Prompt generated: 你是一个Python编程专家...
✓ Error analyzed: 💡 **变量名错误**...
✓ Code explained: 📝 这是一个函数定义...

📍 Test 3: Check File Structure
✓ index.html: 4660 bytes
✓ debug.html: 2240 bytes
✓ explain.html: 1815 bytes
...
```

---

#### `test_simple.py` (73行)
**功能**: 简单API测试脚本

**作用**:
- 测试API端点的基本功能
- 验证HTTP响应

**如何使用**:
```bash
python3 test_simple.py
```

**测试内容**:
- 首页加载
- 调试页加载
- 解释页加载
- API端点测试

---

#### `test_api.py` (75行)
**功能**: 完整API测试脚本

**作用**:
- 使用FastAPI TestClient测试所有API端点
- 测试AI集成功能

**如何使用**:
```bash
python3 test_api.py
```

**注意**: 需要安装httpx模块：
```bash
pip3 install httpx
```

---

#### `__init__.py` (216字节)
**功能**: Python包初始化文件

**作用**:
- 标识目录为Python包
- 允许从目录导入模块

**内容**:
```python
# AI Code Helper包初始化文件
```

---

#### `ai_integration_example.py` (7KB)
**功能**: AI集成示例代码

**作用**:
- 展示如何集成Claude API
- 展示如何集成OpenAI API
- 展示如何集成Hermes API
- 提供Mock模式示例

**包含的内容**:
1. **Claude API集成示例**
2. **OpenAI API集成示例**
3. **Hermes API集成示例**
4. **统一集成框架**

**使用方法**:
```python
from ai_integration_example import ClaudeAIService, OpenAIService

# 使用Claude API
claude_service = ClaudeAIService(api_key="your-key")
response = claude_service.generate_code("写一个函数", "Python")

# 使用OpenAI API
openai_service = OpenAIService(api_key="your-key")
response = openai_service.generate_code("写一个函数", "Python")
```

---

#### `huge_dataset.py` (1.2KB)
**功能**: 大型数据集生成示例

**作用**:
- 演示如何处理大型数据集
- 提供数据生成和处理的参考代码
- 包含生成10000条数据的示例

**使用方法**:
```python
python3 huge_dataset.py
```

**输出**:
- 生成10000条模拟数据
- 数据包含：ID、时间戳、分类、数值等
- 可以用于测试和性能分析

---

## 📁 templates/ 目录文件说明

### `index.html` (109行, 4660字节)
**功能**: 代码生成页面

**作用**:
- 提供代码生成的用户界面
- 用户输入需求和选择编程语言
- 展示AI生成的代码

**页面布局**:
```
┌─────────────────────────────────┐
│   AI Code Helper - 代码生成     │
├─────────────────────────────────┤
│   需求输入框                     │
│   语言选择器                     │
│   [生成代码] 按钮                │
│                                   │
│   生成的代码显示区               │
│   [复制] [下载] 按钮             │
└─────────────────────────────────┘
```

**表单字段**:
- `requirement`: 需求描述文本框
- `language`: 编程语言选择器

**操作按钮**:
- 生成代码：调用 `/api/generate-code` 端点
- 复制代码：复制到剪贴板
- 下载代码：下载为 `.py` 文件

---

### `debug.html` (59行, 2240字节)
**功能**: 自动调试页面

**作用**:
- 用户粘贴错误信息
- AI自动分析错误并修复代码
- 展示错误分析和修复后的代码

**页面布局**:
```
┌─────────────────────────────────┐
│   AI Code Helper - 自动调试     │
├─────────────────────────────────┤
│   错误信息输入框                 │
│   出错代码输入框                 │
│   [分析并修复] 按钮              │
│                                   │
│   错误分析结果                   │
│   修复后的代码                   │
│   [复制] [下载] 按钮             │
└─────────────────────────────────┘
```

**表单字段**:
- `error`: 错误信息文本框
- `code`: 出错代码文本框

**API调用**:
- `POST /api/debug-code`

---

### `explain.html` (53行, 1815字节)
**功能**: 代码解释页面

**作用**:
- 逐行解释代码，帮助新手理解
- 用户输入代码，选择要解释的行
- 展示逐行的详细解释

**页面布局**:
```
┌─────────────────────────────────┐
│   AI Code Helper - 代码解释     │
├─────────────────────────────────┤
│   代码输入框                     │
│   行号选择器                     │
│   [解释] 按钮                    │
│                                   │
│   逐行解释结果                   │
│   [复制] [下载] 按钮             │
└─────────────────────────────────┘
```

**表单字段**:
- `code`: 完整代码文本框
- `line_number`: 要解释的行号

**API调用**:
- `POST /api/explain-line`

---

## 📁 static/ 目录文件说明

### `style.css` (306行, 4955字节)
**功能**: 应用主样式表

**作用**:
- 定义页面的整体样式
- 提供响应式设计
- 美化用户界面

**主要内容**:
1. **重置样式** - 浏览器默认样式重置
2. **布局样式** - Flexbox布局
3. **组件样式** - 按钮、表单、卡片等
4. **响应式设计** - 适配不同屏幕尺寸

**主要样式**:
```css
/* 主容器 */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* 卡片样式 */
.card {
    background: #f5f5f5;
    padding: 20px;
    margin: 10px 0;
    border-radius: 5px;
}

/* 按钮样式 */
.btn {
    background: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
}

/* 输入框样式 */
input, textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 3px;
}
```

---

### `app.js` (248行, 8121字节)
**功能**: 前端JavaScript逻辑

**作用**:
- 处理页面交互逻辑
- 发送AJAX请求到后端API
- 显示和操作生成的代码

**主要功能**:

1. **发送代码生成请求**
```javascript
async function generateCode() {
    const requirement = document.getElementById('requirement').value;
    const language = document.getElementById('language').value;

    const response = await fetch('/api/generate-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ requirement, language })
    });

    const data = await response.json();
    displayCode(data.code);
}
```

2. **发送调试请求**
```javascript
async function debugCode() {
    const error = document.getElementById('error').value;
    const code = document.getElementById('code').value;

    const response = await fetch('/api/debug-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error, code })
    });

    const data = await response.json();
    displayResult(data.analysis, data.fixed_code);
}
```

3. **发送解释请求**
```javascript
async function explainLine() {
    const code = document.getElementById('code').value;
    const lineNumber = document.getElementById('lineNumber').value;

    const response = await fetch('/api/explain-line', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, line_number: lineNumber })
    });

    const data = await response.json();
    displayExplanation(data.explanation);
}
```

4. **复制代码到剪贴板**
```javascript
async function copyCode() {
    const code = document.getElementById('code').textContent;
    await navigator.clipboard.writeText(code);
    alert('代码已复制！');
}
```

5. **下载代码文件**
```javascript
function downloadCode() {
    const code = document.getElementById('code').textContent;
    const blob = new Blob([code], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'code.py';
    a.click();
}
```

---

## 📁 english-prompt-library/ 目录文件说明

### `index.html` (10531字节)
**功能**: 提示词模板库主页

**作用**:
- 提供预构建的AI提示词模板
- 用户可以浏览、搜索、复制模板
- 支持分类浏览

**主要功能**:
1. **分类浏览** - 按类别显示模板（代码生成、调试、解释等）
2. **搜索功能** - 快速搜索模板
3. **模板复制** - 一键复制模板到剪贴板
4. **自定义模板** - 保存用户创建的模板
5. **双语支持** - 支持中英文模板

**页面结构**:
```
┌─────────────────────────────────┐
│   📚 AI提示词模板库              │
├─────────────────────────────────┤
│   [搜索框] [分类筛选]           │
│                                   │
│   ┌───────────────────────┐     │
│   │  代码生成模板         │     │
│   │  ┌─────────────────┐  │     │
│   │  │ 简单函数生成    │  │     │
│   │  │ 复杂逻辑实现    │  │     │
│   │  └─────────────────┘  │     │
│   └───────────────────────┘     │
│                                   │
│   ┌───────────────────────┐     │
│   │  调试模板            │     │
│   │  ┌─────────────────┐  │     │
│   │  │ 语法错误修复    │  │     │
│   │  │ 运行时错误分析  │  │     │
│   │  └─────────────────┘  │     │
│   └───────────────────────┘     │
└─────────────────────────────────┘
```

---

### `style.css` (8390字节)
**功能**: 提示词模板库样式表

**作用**:
- 美化模板库的UI
- 提供现代化的界面设计
- 实现侧边栏导航

**主要样式**:
- 渐变背景
- 卡片式布局
- 响应式设计
- 平滑动画

---

### `app.js` (58032字节)
**功能**: 提示词模板库逻辑

**作用**:
- 加载和管理模板数据
- 实现搜索和过滤功能
- 处理模板复制和保存

**主要功能**:

1. **加载模板数据**
```javascript
const templates = {
    code_generation: [
        {
            id: 1,
            title: "简单函数生成",
            content: "请写一个[语言]函数...",
            category: "代码生成"
        },
        // 更多模板...
    ],
    debugging: [
        // 更多调试模板...
    ],
    explanation: [
        // 更多解释模板...
    ]
};

function loadTemplates() {
    // 从localStorage加载自定义模板
    // 合并预构建模板
}
```

2. **搜索功能**
```javascript
function searchTemplates(query) {
    const results = templates.filter(t =>
        t.title.includes(query) || t.content.includes(query)
    );
    renderTemplates(results);
}
```

3. **复制模板**
```javascript
function copyTemplate(template) {
    navigator.clipboard.writeText(template.content);
    alert('模板已复制！');
}
```

4. **保存自定义模板**
```javascript
function saveCustomTemplate(title, content) {
    const customTemplate = {
        id: Date.now(),
        title,
        content,
        category: '自定义'
    };
    
    customTemplates.push(customTemplate);
    localStorage.setItem('customTemplates', JSON.stringify(customTemplates));
}
```

---

## 📁 examples/ 目录文件说明

### `portfolio_manager.py` (7KB)
**功能**: 投资组合管理器示例

**作用**:
- 演示如何创建一个完整的应用
- 展示数据处理和可视化功能
- 提供实际可用的投资组合管理工具

**主要功能**:
1. **投资组合计算**
2. **风险分析**
3. **收益计算**
4. **可视化图表**

**使用方法**:
```python
python3 examples/portfolio_manager.py
```

**输入**:
- 股票代码
- 买入价格
- 持有数量
- 当前价格

**输出**:
- 投资组合汇总
- 盈亏计算
- 可视化图表

---

### `stock_analyzer.py` (16KB)
**功能**: 股票分析器示例

**作用**:
- 演示如何处理和分析股票数据
- 展示数据处理和统计分析功能
- 提供实用的股票分析工具

**主要功能**:
1. **股票数据获取**
2. **技术指标计算**
3. **趋势分析**
4. **数据可视化**

**使用方法**:
```python
python3 examples/stock_analyzer.py
```

**支持的功能**:
- 移动平均线计算
- RSI指标计算
- MACD指标计算
- K线图绘制

---

### `weather_app.py` (5.9KB)
**功能**: 天气应用示例

**作用**:
- 演示如何集成外部API
- 展示异步编程的使用
- 提供实用的天气查询工具

**主要功能**:
1. **天气查询**
2. **预报显示**
3. **城市切换**
4. **历史数据**

**使用方法**:
```python
python3 examples/weather_app.py
```

**支持的功能**:
- 多城市天气查询
- 每日天气预报
- 历史天气数据
- 图表展示

---

### `calculator_app.py` (9.6KB)
**功能**: 计算器应用示例

**作用**:
- 演示GUI应用开发
- 展示事件处理和状态管理
- 提供一个简单的计算器工具

**主要功能**:
1. **基本计算**
2. **科学计算**
3. **历史记录**
4. **主题切换**

**使用方法**:
```python
python3 examples/calculator_app.py
```

**功能特点**:
- 支持加减乘除
- 支持科学计算（平方根、幂等）
- 历史记录功能
- 多种主题风格

---

## 📁 data/ 目录文件说明

### `python_basics_tutorial.py` (583行, 13KB)
**功能**: Python基础教程

**作用**:
- 系统教授Python编程基础知识
- 提供完整的代码示例
- 包含练习和示例

**教程内容**:

**第一章：Python基础语法**
- 变量与数据类型
- 字符串操作
- 条件语句
- 循环语句
- 函数

**第二章：数据结构**
- 列表操作
- 字典操作
- 集合操作

**第三章：面向对象编程**
- 类与对象
- 继承
- 多态
- 类方法与静态方法

**第四章：文件操作**
- 文件读写
- JSON处理
- Excel读写

**第五章：错误处理**
- try/except
- 异常类型
- 自定义异常

**第六章：模块与包**
- 导入模块
- 标准库使用

**第七章：实用工具**
- 装饰器
- 生成器
- 上下文管理器

**使用方法**:
```python
python3 data/python_basics_tutorial.py
```

---

### `javascript_tutorial.js` (580行, 10KB)
**功能**: JavaScript教程

**作用**:
- 教授JavaScript编程基础
- 包含现代JavaScript特性
- 提供大量实例

**教程内容**:

**第一章：JavaScript基础**
- 变量与数据类型
- 字符串操作
- 数组操作
- 对象操作
- 函数

**第二章：DOM操作**
- 元素选择
- 事件处理
- 样式修改

**第三章：异步编程**
- Promise
- async/await
- Fetch API

**第四章：ES6+新特性**
- 解构赋值
- 展开运算符
- 类
- 模块
- Map和Set

**第五章：HTTP请求**
- Fetch API
- XMLHttpRequest
- 代理配置

**第六章：DOM菜单**
- 创建菜单
- 添加事件

**第七章：表单处理**
- 表单验证
- 数据提交

**使用方法**:
在浏览器中打开：
```bash
python3 -m http.server 8000
# 访问 http://localhost:8000/data/javascript_tutorial.js
```

---

### `ml_tutorial.py` (437行, 12KB)
**功能**: 机器学习教程

**作用**:
- 介绍机器学习基础
- 使用Scikit-learn示例
- 包含数据可视化和模型训练

**教程内容**:

**第一章：NumPy基础**
- 数组操作
- 数组运算
- 索引和切片

**第二章：线性回归**
- 数据生成
- 模型训练
- 预测和评估

**第三章：逻辑回归**
- 分类问题
- 决策边界
- 模型评估

**第四章：K-means聚类**
- 聚类算法
- 可视化聚类结果

**第五章：PCA降维**
- 降维原理
- 主成分分析
- 可视化降维结果

**第六章：决策树**
- 分类树
- 可视化决策树

**第七章：随机森林**
- 集成学习
- 特征重要性

**第八章：神经网络**
- MLP分类器
- 模型评估

**第九章：时间序列分析**
- 趋势分析
- 移动平均
- 窗口聚合

**使用方法**:
```python
python3 data/ml_tutorial.py
```

---

### `excel_processing_tutorial.py` (425行, 12KB)
**功能**: Excel数据处理教程

**作用**:
- 使用pandas处理Excel数据
- 数据清洗和转换
- 数据分析和可视化

**教程内容**:

**第一章：Pandas基础**
- DataFrame操作
- CSV和Excel读写
- 数据探索

**第二章：数据清洗**
- 处理缺失值
- 处理重复值
- 处理异常值

**第三章：数据转换**
- 数据类型转换
- 字符串操作
- 条件转换

**第四章：数据分组和聚合**
- GroupBy操作
- 聚合函数
- 多层分组

**第五章：数据透视表**
- Pivot Table
- 多个聚合函数

**第六章：数据合并**
- SQL风格的合并
- 连接操作

**第七章：数据可视化**
- 柱状图
- 折线图
- 散点图
- 箱线图

**第八章：Excel导入导出**
- 保存为Excel
- 多Sheet导出
- CSV/JSON导出

**第九章：高级应用**
- 时间序列分析
- 窗口聚合

**使用方法**:
```python
python3 data/excel_processing_tutorial.py
```

---

### `database_tutorial.py` (396行, 15KB)
**功能**: 数据库操作教程

**作用**:
- 使用SQLite数据库
- 介绍数据库设计和优化
- 提供完整的CRUD示例

**教程内容**:

**第一章：SQLite基础**
- 创建数据库
- 创建表
- 插入数据

**第二章：CRUD操作**
- 创建记录
- 读取记录
- 更新记录
- 删除记录

**第三章：SQL查询优化**
- SELECT查询
- JOIN查询
- 聚合查询

**第四章：事务处理**
- 事务管理
- 提交和回滚

**第五章：MySQL操作**
- 连接MySQL
- 创建表
- CRUD操作

**第六章：PostgreSQL操作**
- 连接PostgreSQL
- 数据类型
- 高级查询

**第七章：ORM使用**
- SQLAlchemy示例
- 数据模型定义
- 数据库操作

**使用方法**:
```python
python3 data/database_tutorial.py
```

---

### `web_framework_tutorial.py` (388行, 16KB)
**功能**: Web框架教程

**作用**:
- 介绍Flask、Django、FastAPI
- 提供完整的Web开发示例
- 包含认证和API设计

**教程内容**:

**第一章：Flask基础**
- 应用创建
- 路由定义
- 模板渲染

**第二章：Flask模板**
- Jinja2模板
- 继承和包含
- 过滤器和测试器

**第三章：Flask表单**
- 表单处理
- 验证
- CSRF保护

**第四章：Flask数据库**
- 数据库模型
- CRUD操作
- 迁移

**第五章：Django基础**
- 项目创建
- URL配置
- 视图和模板

**第六章：Django模板**
- 模板继承
- 模板标签
- 模板过滤器

**第七章：FastAPI基础**
- 路由定义
- 请求处理
- 响应

**第八章：FastAPI数据库**
- Pydantic模型
- 数据库操作
- CRUD端点

**使用方法**:
```python
python3 data/web_framework_tutorial.py
```

---

### `web_scraping_example.py` (366行, 13KB)
**功能**: Web Scraping示例

**作用**:
- 使用BeautifulSoup抓取网页
- 处理HTTP请求
- 介绍异步抓取

**教程内容**:

**第一章：Requests基础**
- GET请求
- POST请求
- 状态码和响应头

**第二章：BeautifulSoup基础**
- 解析HTML
- 查找元素
- 遍历DOM

**第三章：解析网页内容**
- 提取链接
- 提取图片
- 提取文本

**第四章：爬取多个页面**
- 循环爬取
- 链接管理
- 错误处理

**第五章：提取图片**
- 下载图片
- 批量下载

**第六章：API数据抓取**
- REST API
- JSON数据
- 错误处理

**第七章：浏览器自动化**
- Selenium示例
- 元素定位
- 测试自动化

**第八章：代理和Cookies**
- 代理设置
- Cookie管理
- 会话管理

**第九章：错误处理和重试**
- 异常捕获
- 重试机制
- 限流

**使用方法**:
```python
python3 data/web_scraping_example.py
```

---

### `full_stack_tutorial.py` (500行, 22KB)
**功能**: 全栈开发教程

**作用**:
- 完整的全栈开发指南
- 涵盖前端、后端、DevOps
- 包含最佳实践

**教程内容**:

**第一章：前端开发基础**
- HTML5/CSS3/JavaScript
- React框架
- 状态管理

**第二章：后端开发基础**
- REST API设计
- 认证授权
- 数据验证

**第三章：数据库设计**
- ER图设计
- 设计原则
- 优化策略

**第四章：系统架构**
- 微服务架构
- 事件驱动架构

**第五章：性能优化**
- 数据库优化
- 应用优化
- 缓存策略

**第六章：安全实践**
- 认证授权
- 数据保护

**第七章：测试策略**
- 单元测试
- 集成测试
- E2E测试

**第八章：部署运维**
- Docker容器化
- Kubernetes部署
- CI/CD

**第九章：常见问题**
- 性能问题
- 安全问题

**使用方法**:
```python
python3 data/full_stack_tutorial.py
```

---

### `comprehensive_guide.md` (50KB)
**功能**: 综合开发指南

**作用**:
- 完整的开发指南文档
- 包含所有技术的详细说明
- 提供最佳实践

**主要内容**:
- 架构模式
- 设计原则
- 性能优化
- 安全实践
- 测试策略
- 部署运维
- 常见问题

---

## 📁 其他目录和文件

### `requirements.txt`
**功能**: Python依赖管理

**作用**:
- 列出项目所需的所有Python包
- 便于快速安装依赖

**内容**:
```txt
fastapi==0.104.1           # Web框架
uvicorn[standard]==0.24.0  # ASGI服务器
jinja2==3.1.2              # 模板引擎
python-multipart==0.0.6    # 文件上传
aiofiles==23.2.1           # 异步文件操作
pytest==7.4.3              # 测试框架
pytest-asyncio==0.21.1     # 异步测试
black==23.12.1             # 代码格式化
flake8==6.1.0              # 代码检查
isort==5.13.2              # import排序
```

**安装依赖**:
```bash
pip3 install -r requirements.txt
```

---

### `run.sh`
**功能**: Linux/Mac启动脚本

**作用**:
- 一键启动应用
- 自动切换到项目目录

**内容**:
```bash
#!/bin/bash
cd /Users/mac/Desktop/ai-code-helper
python3 app.py
```

**使用方法**:
```bash
chmod +x run.sh
./run.sh
```

---

### `run.bat`
**功能**: Windows启动脚本

**作用**:
- 一键启动应用（Windows）
- 自动切换到项目目录

**内容**:
```bat
@echo off
cd /d C:\Users\mac\Desktop\ai-code-helper
python app.py
```

**使用方法**:
```bat
run.bat
```

---

### `run.sh.bash`
**功能**: Bash启动脚本（备用）

**作用**:
- 提供另一个启动选项

---

### `README.md`
**功能**: 项目说明文档

**作用**:
- 项目简介
- 功能说明
- 快速开始
- 项目结构
- AI集成说明

**主要内容**:
- 项目概述
- 快速开始指南
- 项目结构
- 核心功能
- AI集成
- 学习资源
- 性能指标
- 贡献指南

---

### `CLAUDE.md`
**功能**: Claude Code开发文档

**作用**:
- 为Claude Code提供项目指导
- 说明项目架构和开发规范

**主要内容**:
- 项目概述
- 项目结构
- 开发命令
- 架构说明
- AI API集成
- 添加新功能
- 测试策略
- 重要说明

---

### `CONTRIBUTING.md`
**功能**: 贡献指南

**作用**:
- 指导如何贡献代码
- 贡献流程
- 代码规范

**主要内容**:
- 如何贡献
- 贡献流程
- 代码规范
- Pull Request流程

---

### `PROJECT_STATUS.md`
**功能**: 项目状态文档

**作用**:
- 项目完成情况总结
- 已完成功能
- 待完成功能

**主要内容**:
- 项目概述
- 已完成功能
- 项目统计
- 核心特性
- 技术实现
- 快速开始
- 待完成功能

---

### `LICENSE`
**功能**: MIT许可证

**作用**:
- 定义项目使用许可
- 规范使用和分发规则

**内容**:
```
MIT License

Copyright (c) 2023 AI Code Helper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

### `CLEANUP_INSTRUCTIONS.md`
**功能**: 清理说明

**作用**:
- 说明项目清理过程
- 清理方案和结果

**主要内容**:
- 当前状态
- 清理方案
- 清理后效果
- 选择建议

---

### `CLEAN_GITHUB_README.md`
**功能**: GitHub专用README

**作用**:
- 面向GitHub用户的README
- 简洁明了的项目说明

**主要内容**:
- 项目简介
- 快速开始
- 项目结构
- 核心功能
- AI集成
- 学习资源
- 性能指标
- 贡献指南

---

### `FINAL_REPORT.md`
**功能**: 最终项目报告

**作用**:
- 项目完成总结
- 清理过程记录
- 项目亮点

**主要内容**:
- 项目状态总结
- 已完成内容
- 需要注意内容
- 清理建议
- 项目亮点
- 下一步建议

---

### `TEST_REPORT.md`
**功能**: 测试报告

**作用**:
- 详细记录测试过程和结果
- 项目状态验证

**主要内容**:
- 测试概览
- 详细测试结果
- 核心功能验证
- 依赖检查
- 项目结构
- 使用说明
- 测试结论

---

## 📊 文件统计

### 代码行数统计

| 类型 | 文件数 | 总行数 |
|------|--------|--------|
| Python文件 | 6 | ~785 |
| HTML文件 | 4 | ~221 |
| CSS文件 | 2 | ~343 |
| JavaScript文件 | 2 | ~628 |
| 教程文件 | 9 | ~3,800 |
| 文档文件 | 10 | ~2,500 |
| **总计** | **33** | **~8,300** |

### 文件大小统计

| 类型 | 总大小 |
|------|--------|
| 代码文件 | ~25 MB |
| 文档文件 | ~6 MB |
| 教程文件 | ~60 MB |
| **总计** | **~91 MB** |

---

## 🚀 快速开始指南

### 1. 安装依赖

```bash
cd /Users/mac/Desktop/ai-code-helper
pip3 install -r requirements.txt
```

### 2. 启动应用

```bash
# 方法1：使用Python
python3 app.py

# 方法2：使用脚本
./run.sh  # Linux/Mac
run.bat   # Windows
```

### 3. 访问应用

```
主应用: http://localhost:8000
```

### 4. 运行测试

```bash
# 手动测试
python3 test_manual.py

# 简单API测试
python3 test_simple.py

# 完整API测试
python3 test_api.py
```

### 5. 浏览提示词库

```bash
python3 -m http.server 8001 -d english-prompt-library
# 访问 http://localhost:8001
```

---

## 📚 教程学习路径

### 初学者

1. **Python基础教程** (`python_basics_tutorial.py`)
2. **JavaScript教程** (`javascript_tutorial.js`)
3. **使用主应用** - 体验代码生成功能
4. **使用提示词库** - 浏览模板

### 中级开发者

1. **Web Scraping示例** (`web_scraping_example.py`)
2. **Excel处理教程** (`excel_processing_tutorial.py`)
3. **数据库教程** (`database_tutorial.py`)
4. **Web框架教程** (`web_framework_tutorial.py`)

### 高级开发者

1. **全栈开发教程** (`full_stack_tutorial.py`)
2. **机器学习教程** (`ml_tutorial.py`)
3. **示例项目分析** (`portfolio_manager.py`, `stock_analyzer.py`)
4. **架构设计指南** (`comprehensive_guide.md`)

---

## 🎯 最佳实践

### 1. 开发规范

- 遵循PEP 8代码规范
- 添加详细的文档字符串
- 编写单元测试
- 使用类型注解

### 2. AI集成

```python
# 使用Claude API
import anthropic

client = anthropic.Anthropic(api_key="your-key")
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=2048,
    messages=[{"role": "user", "content": prompt}]
)
```

### 3. 代码管理

```bash
# 安装依赖
pip install -r requirements.txt

# 代码格式化
black app.py utils.py

# 代码检查
flake8 app.py utils.py

# 导入排序
isort app.py utils.py
```

### 4. 项目发布

1. 清理项目（运行 `CLEANUP_SCRIPT.py`）
2. 测试应用（运行 `test_manual.py`）
3. 更新README（使用 `CLEAN_GITHUB_README.md`）
4. 添加测试（编写单元测试）
5. 提交到Git

---

## 📞 获取帮助

### 文档

- `README.md` - 项目说明
- `CLAUDE.md` - Claude Code文档
- `TEST_REPORT.md` - 测试报告
- `COMPREHENSIVE_GUIDE.md` - 综合指南

### 测试脚本

- `test_manual.py` - 完整功能测试
- `test_simple.py` - 简单API测试

### 示例

- `examples/` - 完整的示例项目
- `data/` - 详细的学习教程

---

**文档版本**: 1.0  
**最后更新**: 2026-07-13  
**维护者**: AI Code Helper Team
