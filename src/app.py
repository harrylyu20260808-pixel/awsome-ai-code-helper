"""
AI编程助手 - 核心后端程序
面向编程新手：表单式代码生成、自动调试、逐行解释
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from utils import generate_code_prompt, analyze_error, explain_code_line
import os
import json

# 1. 创建FastAPI应用
app = FastAPI(title="AI Code Helper", description="面向编程新手的AI编程助手")

# 2. 配置模板目录
templates = Jinja2Templates(directory="templates")

# 3. 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# ===================================
# 页面路由
# ===================================

@app.get("/")
async def home(request: Request):
    """首页：代码生成界面"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/debug")
async def debug_page(request: Request):
    """调试页面"""
    return templates.TemplateResponse("debug.html", {"request": request})

@app.get("/explain")
async def explain_page(request: Request, code: str = ""):
    """解释页面：逐行解释代码"""
    return templates.TemplateResponse("explain.html", {
        "request": request,
        "initial_code": code
    })

# ===================================
# API路由
# ===================================

@app.post("/api/generate-code")
async def generate_code(request: Request):
    """API: 生成代码"""
    data = await request.json()
    requirement = data.get("requirement", "")
    language = data.get("language", "Python")

    # 生成prompt
    prompt = generate_code_prompt(requirement, language)

    # 调用AI（这里预留接口，用户自己实现）
    ai_response = await call_ai(prompt)

    return JSONResponse({
        "code": ai_response,
        "explanation": '生成成功！点击"查看解释"按钮可以逐行了解代码。'
    })

@app.post("/api/debug-code")
async def debug_code(request: Request):
    """API: 修复代码"""
    data = await request.json()
    code = data.get("code", "")
    error = data.get("error", "")

    # 分析错误
    analysis = analyze_error(error)

    # 生成修复后的代码
    prompt = f"""你是一个编程专家。用户遇到以下错误，请修复代码：

错误信息：
{error}

代码：
{code}

请返回修复后的完整代码，不要添加任何解释。"""

    fixed_code = await call_ai(prompt)

    return JSONResponse({
        "analysis": analysis,
        "fixed_code": fixed_code,
        "explanation": analysis + " 已自动修复！"
    })

@app.post("/api/explain-line")
async def explain_line(request: Request):
    """API: 解释单行代码"""
    data = await request.json()
    code = data.get("code", "")
    line_number = data.get("line_number", 1)

    explanation = explain_code_line(code, line_number)

    return JSONResponse({"explanation": explanation})

# ===================================
# AI调用接口（预留，用户自己实现）
# ===================================

async def call_ai(prompt: str) -> str:
    """
    调用AI生成代码
    用户在这里接入 Claude API 或 Hermes API

    使用示例（Claude API）：
    """
    try:
        # ===== 用户在这里替换为实际的API调用 =====
        # 这里是一个示例框架

        # import anthropic
        # client = anthropic.Anthropic(api_key="your-api-key-here")
        # response = client.messages.create(
        #     model="claude-3-5-sonnet-20241022",
        #     max_tokens=2048,
        #     messages=[{"role": "user", "content": prompt}]
        # )
        # return response.content[0].text

        # ===== 临时返回示例代码（用户需要接入真实API）=====
        if "Python" in prompt or "python" in prompt:
            return f"""# 这是AI生成的代码示例
def hello_world():
    print("Hello, World!")
    return "Hello, World!"

# 运行示例
if __name__ == "__main__":
    result = hello_world()
    print(f"结果: {result}")
"""
        elif "JavaScript" in prompt or "javascript" in prompt:
            return f"""// 这是AI生成的代码示例
function helloWorld() {{
    console.log("Hello, World!");
    return "Hello, World!";
}}

// 运行示例
helloWorld();
"""
        else:
            return "# 这是AI生成的代码示例\nprint('Hello, World!')"

    except Exception as e:
        return f"# 错误: {{e}}\n# 请在 app.py 的 call_ai() 函数中接入真实的AI API"

if __name__ == "__main__":
    # 启动服务器
    import uvicorn
    print("🚀 AI编程助手启动中...")
    print("📍 访问地址: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
