[README.md](https://github.com/user-attachments/files/30002374/README.md)
# AI Code Helper - AI Programming Assistant

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/harrylyu20260808-pixel/awsome-ai-code-helper?style=social)
![GitHub forks](https://img.shields.io/github/forks/harrylyu20260808-pixel/awsome-ai-code-helper?style=social)
![GitHub issues](https://img.shields.io/github/issues/harrylyu20260808-pixel/awsome-ai-code-helper)
![GitHub license](https://img.shields.io/github/license/harrylyu20260808-pixel/awsome-ai-code-helper)
![Python version](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![Code style](https://img.shields.io/badge/code%20style-black-000000)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[中文文档](#中文文档) | [English Docs](#english-documentation)

An intelligent programming assistant for beginners, featuring code generation, automatic debugging, and code explanation - all without needing to write prompts or understand debugging.

</div>

---

## ✨ Core Features

- **📝 Code Generation** - Simply enter requirements and AI generates code automatically
- **🐛 Auto Debugging** - Paste error messages and AI automatically fixes your code
- **📖 Line-by-Line Explanation** - AI explains each line of code, beginner-friendly
- **📚 Prompt Template Library** - 60+ pre-built templates with custom support

## 🚀 Quick Start

### Requirements

- Python 3.8+
- pip package manager
- Modern browser

### Installation

```bash
# 1. Clone or download the project
cd ai-code-helper

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure AI API (optional, uses Mock mode by default)
# Edit the call_ai() function in app.py

# 4. Start the server
python app.py

# 5. Access the application
# Open browser: http://localhost:8000
```

### Prompt Template Library

```bash
# Open directly in browser
open english-prompt-library/index.html

# Or use local server
python3 -m http.server 8001 -d english-prompt-library
```

## 📁 Project Structure

```
ai-code-helper/ 
├── app.py                    # FastAPI backend (main web app)
├── utils.py                  # Core utilities: prompts, error analysis, code explanation
├── requirements.txt          # Python dependencies
├── templates/                # HTML templates
│   ├── index.html            # Home page (code generation)
│   ├── debug.html            # Debug page (error analysis)
│   └── explain.html          # Explain page (code explanation)
├── static/                   # Static resources
│   ├── style.css             # Stylesheet
│   └── app.js                # JavaScript logic
├── english-prompt-library/   # Prompt template library
│   ├── index.html            # Template library interface
│   ├── style.css             # Stylesheet
│   ├── app.js                # JavaScript logic
│   └── README.md             # Library documentation
├── data/                     # Learning resources & tutorials
│   ├── python_basics_tutorial.py
│   ├── javascript_tutorial.js
│   ├── ml_tutorial.py
│   ├── excel_processing_tutorial.py
│   ├── database_tutorial.py
│   ├── web_framework_tutorial.py
│   ├── web_scraping_example.py
│   └── comprehensive_guide.md
├── examples/                 # Example projects
│   ├── portfolio_manager.py
│   ├── stock_analyzer.py
│   ├── weather_app.py
│   └── calculator_app.py
├── modules/                  # Modular code
│   └── calculator_app.py
├── apps/                     # Application examples
│   ├── portfolio_manager.py
│   ├── stock_analyzer.py
│   └── weather_app.py
├── docs/                     # Documentation
│   ├── API.md
│   ├── DEPLOYMENT.md
│   └── CONTRIBUTING.md
├── tests/                    # Tests
├── CLAUDE.md                 # Claude Code documentation
├── README.md                 # This file
├── PROJECT_STATUS.md         # Project status
└── LICENSE                   # MIT License
```

## 🎯 Core Functionality

### 1. Code Generation

```
Requirements → AI generates code → View explanation → Copy/Download
```

### 2. Auto Debugging

```
Error message + Code → AI analyzes and fixes → Copy/Download
```

### 3. Code Explanation

```
Input code → Line-by-line explanation → Understand each line
```

## 🔧 AI Integration

The project provides AI integration interfaces supporting:

- **Claude API**
- **OpenAI API**
- **Hermes API**
- **Mock mode** (for demonstration)

### Using Claude API

Edit the `call_ai()` function in `app.py`:

```python
import anthropic
import os

async def call_ai(prompt: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
```

Set environment variable:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### Using OpenAI API

```python
# app.py
import openai
import os

async def call_ai(prompt: str) -> str:
    client = openai.AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2048
    )
    return response.choices[0].message.content
```

Set environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 📚 Learning Resources

The project includes comprehensive learning resources:

- [Python Basics Tutorial](data/python_basics_tutorial.py) - 583 lines
- [JavaScript Tutorial](data/javascript_tutorial.js) - 580 lines
- [Machine Learning Tutorial](data/ml_tutorial.py) - 437 lines
- [Excel Processing Tutorial](data/excel_processing_tutorial.py) - 425 lines
- [Database Tutorial](data/database_tutorial.py) - 396 lines
- [Web Framework Tutorial](data/web_framework_tutorial.py) - 388 lines
- [Web Scraping Tutorial](data/web_scraping_example.py) - 366 lines
- [Full Stack Development Guide](data/full_stack_tutorial.py) - Complete guide
- [Comprehensive Development Guide](data/comprehensive_guide.md) - Complete guide

## 🧪 Testing

```bash
# Run tests
python3 test_api.py

# Or use pytest
pip install pytest
pytest
```

## 📊 Performance

- **Response Time**: < 5 seconds (AI call)
- **Page Load**: < 1 second
- **Concurrent Support**: 10+ users

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

### Development Workflow

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 (Python)
- Use type annotations
- Add docstrings
- Write unit tests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI - Modern web framework
- Jinja2 - Template engine
- Claude API - AI service
- All contributors and users

## 📮 Contact

- **Project Homepage**:https://github.com/harrylyu20260808-pixel/awsome-ai-code-helper
- **Issues**: https://github.com/harrylyu20260808-pixel/awsome-ai-code-helper/issues
- **Email**: HarryLv20260808@outlook.com

---

<div align="center">

**⭐ If you find this project helpful, please give it a Star! ⭐**

Made with ❤️

</div>
