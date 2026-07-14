"""
AI编程助手 - 工具函数
提供代码生成、错误分析、代码解释等功能
"""

def generate_code_prompt(requirement: str, language: str) -> str:
    """
    生成AI调用的prompt
    :param requirement: 用户需求
    :param language: 编程语言
    :return: 生成的prompt
    """
    prompts = {
        "Python": f"""你是一个Python编程专家。请为以下需求生成高质量代码：

需求：{requirement}

要求：
1. 代码要简洁易懂，适合编程新手
2. 添加必要的注释，说明每一步的作用
3. 使用清晰的变量名和函数名
4. 包含一个简单的示例用法

请只返回代码，不要添加任何其他文字说明。""",

        "JavaScript": f"""你是一个JavaScript编程专家。请为以下需求生成高质量代码：

需求：{requirement}

要求：
1. 代码要简洁易懂，适合编程新手
2. 添加必要的注释，说明每一步的作用
3. 使用清晰的变量名和函数名
4. 包含一个简单的示例用法

请只返回代码，不要添加任何其他文字说明。""",

        "Java": f"""你是一个Java编程专家。请为以下需求生成高质量代码：

需求：{requirement}

要求：
1. 代码要简洁易懂，适合编程新手
2. 添加必要的注释，说明每一步的作用
3. 使用清晰的变量名和函数名
4. 包含一个简单的示例用法

请只返回代码，不要添加任何其他文字说明。""",

        "C++": f"""你是一个C++编程专家。请为以下需求生成高质量代码：

需求：{requirement}

要求：
1. 代码要简洁易懂，适合编程新手
2. 添加必要的注释，说明每一步的作用
3. 使用清晰的变量名和函数名
4. 包含一个简单的示例用法

请只返回代码，不要添加任何其他文字说明。""",
    }

    return prompts.get(language, prompts["Python"])

def analyze_error(error_message: str) -> str:
    """
    分析错误信息，返回通俗易懂的解释
    :param error_message: 错误信息
    :return: 人类可读的错误解释
    """
    error_lower = error_message.lower()

    if "syntaxerror" in error_lower:
        return "💡 **语法错误**: 你写的代码格式不对，就像英语句子少了逗号或标点。"
    elif "nameerror" in error_lower:
        return "💡 **变量名错误**: 你使用的变量或函数名写错了，就像你想说话但用了错误的名字。"
    elif "typeerror" in error_lower:
        return "💡 **类型错误**: 你把不同类型的东西混在一起了，就像你想把苹果和鞋子一起吃。"
    elif "indexerror" in error_lower:
        return "💡 **索引错误**: 你试图访问不存在的位置，就像你想打开第10个抽屉但只有5个抽屉。"
    elif "valueerror" in error_lower:
        return "💡 **值错误**: 你给函数传了错误类型的参数，就像你想吃温度计一样。"
    elif "keyerror" in error_lower:
        return "💡 **键错误**: 你在字典中查找不存在的键，就像你想找名字叫'小红'但实际叫'小明'。"
    elif "attributeerror" in error_lower:
        return "💡 **属性错误**: 你调用的对象没有这个功能，就像你想用手机打电话但手机是收音机。"
    else:
        return f"💡 **错误分析**: {error_message[:100]}... 通常是因为代码逻辑或语法有问题。"

def explain_code_line(code: str, line_number: int) -> str:
    """
    逐行解释代码
    :param code: 完整代码
    :param line_number: 要解释的行号（从1开始）
    :return: 该行的解释
    """
    lines = code.split('\n')

    if line_number < 1 or line_number > len(lines):
        return "⚠️ 行号超出范围，请输入1到{}之间的行号".format(len(lines))

    line = lines[line_number - 1]
    stripped_line = line.strip()

    if not stripped_line or stripped_line.startswith('#'):
        return "ℹ️ 这是一个空行或注释行"

    explanations = []

    # 简单的规则引擎
    if stripped_line.startswith('def'):
        explanations.append("📝 这是一个函数定义")
        if '->' in stripped_line:
            function_type = stripped_line.split('->')[1].strip()
            explanations.append(f"➡️ 这个函数会返回：{function_type}")
        explanations.append("⭐ 使用 def 关键字来定义一个函数")
    elif stripped_line.startswith('return'):
        explanations.append("📤 return 是'返回'的意思")
        explanations.append("➡️ 表示函数执行到这里结束，并返回后面的值")
    elif stripped_line.startswith('import'):
        explanations.append("📦 import 是'导入'的意思")
        explanations.append("➡️ 表示从Python的标准库中引入某个模块")
    elif stripped_line.startswith('if'):
        explanations.append("🔍 if 是'如果'的意思")
        explanations.append("➡️ 如果后面的条件为真，就执行下面的代码")
    elif stripped_line.startswith('else'):
        explanations.append("🔄 else 是'否则'的意思")
        explanations.append("➡️ 如果前面的 if 条件不满足，就执行 else 里的代码")
    elif stripped_line.startswith('for'):
        explanations.append("🔁 for 是'遍历'的意思")
        explanations.append("➡️ 用来循环处理一个列表或序列中的每个元素")
    elif stripped_line.startswith('while'):
        explanations.append("⏳ while 是'当...时候'的意思")
        explanations.append("➡️ 当后面的条件为真时，重复执行代码")
    elif stripped_line.startswith('print'):
        explanations.append("🖨️ print 是'打印'的意思")
        explanations.append("➡️ 在屏幕上显示内容，就像写在黑板上一样")
    elif stripped_line.startswith('#'):
        explanations.append("💡 # 是注释符号")
        explanations.append("➡️ 这是给程序员看的说明，程序不会执行")
    else:
        explanations.append("📝 这行代码执行某种操作")
        explanations.append("➡️ 具体功能取决于代码的具体内容")

    return "\n".join(explanations)

def check_syntax(code: str, language: str = "Python") -> dict:
    """
    检查代码语法（简单模拟）
    :param code: 代码内容
    :param language: 编程语言
    :return: 检查结果
    """
    has_undefined_variables = []  # 未定义的变量
    has_unclosed_brackets = []  # 未闭合的括号
    has_unclosed_quotes = []  # 未闭合的引号

    # 简单的检查规则
    lines = code.split('\n')

    for i, line in enumerate(lines):
        stripped = line.strip()

        # 检查括号
        open_brackets = line.count('(') + line.count('[') + line.count('{')
        close_brackets = line.count(')') + line.count(']') + line.count('}')

        if open_brackets != close_brackets:
            has_unclosed_brackets.append(f"第{i+1}行: 括号不匹配")

        # 检查引号
        if line.count('"') % 2 != 0 or line.count("'") % 2 != 0:
            has_unclosed_quotes.append(f"第{i+1}行: 引号未闭合")

    return {
        "valid": len(has_unclosed_brackets) == 0 and len(has_unclosed_quotes) == 0,
        "errors": has_unclosed_brackets + has_unclosed_quotes,
        "warnings": []
    }
