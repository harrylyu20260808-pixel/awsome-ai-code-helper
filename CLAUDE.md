# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Code Helper is a dual-component project for programming beginners:
1. **Main Application**: FastAPI backend with web UI for code generation, debugging, and explanation
2. **Prompt Library**: Pure HTML/CSS/JS frontend with 60+ bilingual prompt templates

The main app is designed to work with AI APIs (Claude, Hermes, etc.) - the AI integration is a placeholder that must be implemented by the user.

## Project Structure

```
ai-code-helper/
├── app.py                    # FastAPI backend (main web app)
├── utils.py                  # Core utilities: prompts, error analysis, code explanation
├── requirements.txt          # Python dependencies
├── __init__.py              # Package initialization
├── 使用说明.md              # Chinese user guide
├── english-prompt-library/  # Separate HTML/CSS/JS prompt template library
│   ├── index.html          # Main prompt library interface
│   ├── style.css           # Styling
│   ├── app.js              # JavaScript logic
│   └── README.md           # Library documentation
└── CLAUDE.md               # This file
```

## Development Commands

### Backend (Main Application)

**Install dependencies:**
```bash
pip3 install -r requirements.txt
```

**Run the server:**
```bash
python3 app.py
```

**Run tests** (when test framework is added):
```bash
pytest  # or py.test
```

**Code formatting (if tools are added):**
```bash
black app.py utils.py  # Example with black formatter
```

### Prompt Library

**View the prompt library:**
```bash
open english-prompt-library/index.html
# or
python3 -m http.server 8001 -d english-prompt-library
# Then visit http://localhost:8001
```

## Architecture

### Backend (FastAPI)

**Entry Point**: `app.py` - FastAPI application with routes for:
- `/` - Home page (code generation form)
- `/debug` - Debug page (error analysis)
- `/explain?code=...` - Explain page (code explanation)

**API Endpoints**:
- `POST /api/generate-code` - Generate code from requirements
- `POST /api/debug-code` - Fix code from error message
- `POST /api/explain-line` - Explain specific line of code

**AI Integration Point**:
- `call_ai()` function in `app.py` (lines 111-157) - User must implement actual API call
- Currently returns placeholder code for demo purposes
- Expected to return code string from AI response

### Core Utilities (`utils.py`)

**Key Functions**:
- `generate_code_prompt(requirement, language)` - Creates AI prompts for 4 languages (Python, JavaScript, Java, C++)
- `analyze_error(error_message)` - Returns beginner-friendly error explanations
- `explain_code_line(code, line_number)` - Line-by-line code explanation using simple rules
- `check_syntax(code, language)` - Basic syntax checking (brackets, quotes)

### Frontend Components

**Main App** (templates/ directory - needs to be created):
- Single-page application with tab navigation
- AJAX calls to FastAPI endpoints
- Code display, copy, and download functionality

**Prompt Library** (english-prompt-library/):
- Pure HTML/CSS/JS, no backend dependencies
- 60+ templates organized by category
- Custom template system with localStorage persistence
- Bilingual (English/Chinese) content

## AI API Integration

**Required Implementation**: User must complete the `call_ai()` function in `app.py`

**Claude API Example**:
```python
import anthropic

async def call_ai(prompt: str) -> str:
    client = anthropic.Anthropic(api_key="your-api-key")
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
```

**Key Requirements**:
- The function is async but currently synchronous
- Return format should be pure code (no conversational filler)
- Handle exceptions appropriately
- API key should be stored in environment variables, not hardcoded

## Adding New Features

### Backend Endpoints

Add routes in `app.py` following the existing pattern. Example:
```python
@app.post("/api/new-endpoint")
async def new_endpoint(request: Request):
    data = await request.json()
    # Your logic here
    return JSONResponse({"result": "success"})
```

### Utility Functions

Add helper functions in `utils.py`. Update the `generate_code_prompt()` function for custom prompts per language.

### Frontend Templates

Create HTML files in `templates/` directory and add corresponding routes in `app.py`. The main app uses Jinja2 templates.

### Prompt Library Templates

Add templates in `english-prompt-library/app.js` by adding objects to the template categories array in the `loadTemplates()` function.

## Testing Strategy

1. **Unit Tests**: Test utility functions (`utils.py`) independently
   - Test prompt generation with various inputs
   - Test error analysis mapping
   - Test line explanation rules

2. **Integration Tests**: Test API endpoints
   - Mock AI responses for `call_ai()`
   - Test request/response formats
   - Verify error handling

3. **Frontend Tests** (when implemented):
   - Test AJAX calls
   - Test template rendering
   - Test user interactions

## Important Notes

- The project has two separate frontends: main app (Jinja2 templates) and prompt library (pure HTML/JS)
- Templates directory (`templates/`) and static files (`static/`) are referenced but may not exist yet
- AI integration is intentionally placeholder - this is a framework for users to connect their own AI API
- Error messages are designed to be beginner-friendly with emojis and simple analogies
- The prompt library is a standalone static site that can be deployed independently
