"""
Simple API Test Script
测试AI Code Helper API的基本功能
"""

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

print("=" * 60)
print("Testing AI Code Helper API")
print("=" * 60)

# Test 1: Home Page
print("\n📍 Test 1: Home Page")
print("-" * 60)
try:
    response = client.get("/")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("✓ Home page loads successfully")
    else:
        print(f"✗ Unexpected status code: {response.status_code}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 2: Debug Page
print("\n📍 Test 2: Debug Page")
print("-" * 60)
try:
    response = client.get("/debug")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("✓ Debug page loads successfully")
    else:
        print(f"✗ Unexpected status code: {response.status_code}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 3: Explain Page
print("\n📍 Test 3: Explain Page")
print("-" * 60)
try:
    response = client.get("/explain?code=print('Hello')")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("✓ Explain page loads successfully")
    else:
        print(f"✗ Unexpected status code: {response.status_code}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 4: API - Generate Code
print("\n📍 Test 4: Generate Code API")
print("-" * 60)
try:
    response = client.post("/api/generate-code",
                         json={"requirement": "Write a simple function", "language": "Python"})
    print(f"Status: {response.status_code}")
    data = response.json()
    if response.status_code == 200:
        print("✓ Generate code API works")
        print(f"Response preview: {str(data)[:100]}...")
    else:
        print(f"✗ API returned error: {data}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 5: API - Debug Code
print("\n📍 Test 5: Debug Code API")
print("-" * 60)
try:
    response = client.post("/api/debug-code",
                         json={"error": "NameError: x is not defined", "code": "print(x)"})
    print(f"Status: {response.status_code}")
    data = response.json()
    if response.status_code == 200:
        print("✓ Debug code API works")
        print(f"Analysis: {data.get('analysis', 'N/A')}")
    else:
        print(f"✗ API returned error: {data}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 6: API - Explain Line
print("\n📍 Test 6: Explain Line API")
print("-" * 60)
try:
    response = client.post("/api/explain-line",
                         json={"code": "def hello():\n    print('Hello')", "line_number": 1})
    print(f"Status: {response.status_code}")
    data = response.json()
    if response.status_code == 200:
        print("✓ Explain line API works")
        print(f"Explanation: {data.get('explanation', 'N/A')}")
    else:
        print(f"✗ API returned error: {data}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 7: Utility Functions
print("\n📍 Test 7: Utility Functions")
print("-" * 60)
try:
    from utils import generate_code_prompt, analyze_error, explain_code_line

    prompt = generate_code_prompt("Write a function", "Python")
    print(f"✓ Prompt generated: {prompt[:80]}...")

    error_analysis = analyze_error("NameError: x is not defined")
    print(f"✓ Error analyzed: {error_analysis}")

    explanation = explain_code_line("def hello():\n    print('Hello')", 1)
    print(f"✓ Code explained: {explanation}")
except Exception as e:
    print(f"✗ Error in utilities: {e}")

print("\n" + "=" * 60)
print("Testing complete!")
print("=" * 60)
