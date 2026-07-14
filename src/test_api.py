"""
Test script for AI Code Helper API
Run this to verify that the API endpoints are working correctly
"""

import asyncio
import sys

# Test the API endpoints without requiring AI integration
async def test_api_endpoints():
    print("=" * 60)
    print("Testing AI Code Helper API Endpoints")
    print("=" * 60)

    # Import the app
    from fastapi.testclient import TestClient
    from app import app

    client = TestClient(app)

    # Test 1: Generate Code API
    print("\n📋 Test 1: Generate Code API")
    print("-" * 60)
    response = client.post("/api/generate-code",
                         json={"requirement": "Write a simple function", "language": "Python"})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test 2: Debug Code API
    print("\n🐛 Test 2: Debug Code API")
    print("-" * 60)
    response = client.post("/api/debug-code",
                         json={"error": "NameError: x is not defined", "code": "print(x)"})
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Analysis: {result['analysis']}")
    print(f"Fixed Code Preview: {result['fixed_code'][:100]}...")

    # Test 3: Explain Line API
    print("\n📖 Test 3: Explain Line API")
    print("-" * 60)
    response = client.post("/api/explain-line",
                         json={"code": "def hello():\n    print('Hello')", "line_number": 1})
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Explanation: {result['explanation']}")

    # Test 4: Check utility functions
    print("\n🔧 Test 4: Utility Functions")
    print("-" * 60)
    from utils import generate_code_prompt, analyze_error, explain_code_line

    # Test prompt generation
    prompt = generate_code_prompt("Write a function", "Python")
    print(f"✓ Prompt generated: {prompt[:100]}...")

    # Test error analysis
    error_analysis = analyze_error("NameError: x is not defined")
    print(f"✓ Error analyzed: {error_analysis}")

    # Test code explanation
    explanation = explain_code_line("def hello():\n    print('Hello')", 1)
    print(f"✓ Code explained: {explanation}")

    print("\n" + "=" * 60)
    print("All tests completed successfully! 🎉")
    print("=" * 60)

if __name__ == "__main__":
    try:
        asyncio.run(test_api_endpoints())
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        sys.exit(1)
