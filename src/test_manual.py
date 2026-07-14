"""
Manual API Testing
手动测试API功能
"""

print("=" * 60)
print("Testing AI Code Helper Components")
print("=" * 60)

# Test 1: Import modules
print("\n📍 Test 1: Import Modules")
print("-" * 60)
try:
    from utils import generate_code_prompt, analyze_error, explain_code_line
    print("✓ All utility functions imported successfully")
except Exception as e:
    print(f"✗ Import error: {e}")

# Test 2: Utility Functions
print("\n📍 Test 2: Test Utility Functions")
print("-" * 60)
try:
    prompt = generate_code_prompt("Write a function", "Python")
    print(f"✓ Prompt generated: {prompt[:80]}...")

    error_analysis = analyze_error("NameError: x is not defined")
    print(f"✓ Error analyzed: {error_analysis}")

    explanation = explain_code_line("def hello():\n    print('Hello')", 1)
    print(f"✓ Code explained: {explanation}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 3: Check file structure
print("\n📍 Test 3: Check File Structure")
print("-" * 60)
files_ok = True

templates = ['index.html', 'debug.html', 'explain.html']
for file in templates:
    import os
    path = f"templates/{file}"
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"✓ {file}: {size} bytes")
    else:
        print(f"✗ {file}: NOT FOUND")
        files_ok = False

static_files = ['style.css', 'app.js']
for file in static_files:
    path = f"static/{file}"
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"✓ {file}: {size} bytes")
    else:
        print(f"✗ {file}: NOT FOUND")
        files_ok = False

prompt_lib = ['index.html', 'style.css', 'app.js']
for file in prompt_lib:
    path = f"english-prompt-library/{file}"
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"✓ {file}: {size} bytes")
    else:
        print(f"✗ {file}: NOT FOUND")
        files_ok = False

if files_ok:
    print("\n✓ All essential files are present")
else:
    print("\n✗ Some files are missing")

# Test 4: Check README
print("\n📍 Test 4: Check Documentation")
print("-" * 60)
import os
doc_files = ['README.md', 'CLAUDE.md', 'requirements.txt', 'LICENSE']
for file in doc_files:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"✓ {file}: {size} bytes")
    else:
        print(f"✗ {file}: NOT FOUND")

print("\n" + "=" * 60)
print("Manual testing complete!")
print("=" * 60)
print("\n📋 Manual Testing Instructions:")
print("1. Run: python3 app.py")
print("2. Visit: http://localhost:8000")
print("3. Test pages:")
print("   - / - Code generation page")
print("   - /debug - Debug page")
print("   - /explain - Code explanation page")
print("4. Test API endpoints:")
print("   - POST /api/generate-code")
print("   - POST /api/debug-code")
print("   - POST /api/explain-line")
