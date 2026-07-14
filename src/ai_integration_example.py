"""
AI Integration Examples for AI Code Helper

This file provides examples of how to integrate different AI APIs
into the call_ai() function in app.py
"""

import asyncio
from typing import Optional

# ============================================================
# Example 1: Claude API Integration
# ============================================================
"""
To use Claude API:
1. Install: pip install anthropic
2. Get API key from: https://console.anthropic.com/
3. Set environment variable: export ANTHROPIC_API_KEY="your-key-here"

Implementation in app.py:
"""

# Example implementation
class ClaudeIntegration:
    def __init__(self, api_key: str):
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=api_key)
        except ImportError:
            print("Error: Install anthropic package: pip install anthropic")
            self.client = None

    async def generate_code(self, prompt: str) -> str:
        """Generate code using Claude API"""
        if not self.client:
            raise ImportError("Anthropic package not installed")

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

# ============================================================
# Example 2: OpenAI API Integration
# ============================================================
"""
To use OpenAI API:
1. Install: pip install openai
2. Get API key from: https://platform.openai.com/
3. Set environment variable: export OPENAI_API_KEY="your-key-here"

Implementation in app.py:
"""

class OpenAIIntegration:
    def __init__(self, api_key: str):
        try:
            import openai
            self.client = openai.AsyncOpenAI(api_key=api_key)
        except ImportError:
            print("Error: Install openai package: pip install openai")
            self.client = None

    async def generate_code(self, prompt: str) -> str:
        """Generate code using OpenAI API"""
        if not self.client:
            raise ImportError("OpenAI package not installed")

        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a coding expert. Generate code only."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2048
        )
        return response.choices[0].message.content

# ============================================================
# Example 3: Hermes API Integration (LLaMA 3 via local server)
# ============================================================
"""
To use Hermes API:
1. Install Hermes: https://github.com/ggerganov/llama.cpp
2. Start Hermes server: ./llama-server -m model.gguf -c 4096
3. Set environment variable: export HERMES_API_URL="http://localhost:8080"

Implementation in app.py:
"""

class HermesIntegration:
    def __init__(self, api_url: str = "http://localhost:8080"):
        self.api_url = api_url

    async def generate_code(self, prompt: str) -> str:
        """Generate code using Hermes API"""
        import httpx

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.api_url,
                json={
                    "prompt": prompt,
                    "max_tokens": 2048,
                    "temperature": 0.7
                },
                timeout=60.0
            )
            response.raise_for_status()
            return response.json().get("response", "")

# ============================================================
# Example 4: Mock Implementation (for testing without AI)
# ============================================================

class MockAI:
    """Mock AI for testing without real API"""

    def __init__(self):
        pass

    async def generate_code(self, prompt: str) -> str:
        """Generate mock code for testing"""
        language = "Python"
        if "JavaScript" in prompt or "javascript" in prompt:
            language = "JavaScript"
        elif "Java" in prompt:
            language = "Java"
        elif "C++" in prompt:
            language = "C++"

        return f"""# Generated Code ({language})
# This is a mock response for testing purposes

def example_function():
    '''Example function'''
    print("Hello from {language}!")

if __name__ == "__main__":
    example_function()
"""

# ============================================================
# Unified Integration Strategy
# ============================================================

class AIIntegration:
    """
    Unified AI integration class that supports multiple providers
    """

    SUPPORTED_PROVIDERS = ["claude", "openai", "hermes", "mock"]

    def __init__(self, provider: str = "mock", **kwargs):
        self.provider = provider.lower()

        if self.provider == "claude":
            api_key = kwargs.get("api_key") or os.environ.get("ANTHROPIC_API_KEY")
            self.ai = ClaudeIntegration(api_key)
        elif self.provider == "openai":
            api_key = kwargs.get("api_key") or os.environ.get("OPENAI_API_KEY")
            self.ai = OpenAIIntegration(api_key)
        elif self.provider == "hermes":
            self.ai = HermesIntegration(
                api_url=kwargs.get("api_url", "http://localhost:8080")
            )
        else:
            self.ai = MockAI()

    async def generate_code(self, prompt: str) -> str:
        """Generate code using the configured AI provider"""
        return await self.ai.generate_code(prompt)

# ============================================================
# Usage Example
# ============================================================

"""
To use in app.py, replace the call_ai() function with:

import os

# Configure AI provider (choose one)
AI_PROVIDER = os.environ.get("AI_PROVIDER", "mock")  # Options: claude, openai, hermes, mock

# Initialize AI integration
ai = AIIntegration(provider=AI_PROVIDER)

async def call_ai(prompt: str) -> str:
    """Generate code using configured AI provider"""
    try:
        return await ai.generate_code(prompt)
    except Exception as e:
        return f"# Error calling AI: {str(e)}\\n# Please check your API configuration"
"""

# Test examples
async def test_ai_providers():
    """Test all AI providers"""

    print("Testing Mock AI...")
    mock_ai = AIIntegration(provider="mock")
    result = await mock_ai.generate_code("Write a Python function")
    print(f"✓ Mock AI: {result[:100]}...")

    print("\nTesting Hermes AI (requires running server)...")
    try:
        hermes_ai = AIIntegration(provider="hermes")
        result = await hermes_ai.generate_code("Write a Python function")
        print(f"✓ Hermes AI: {result[:100]}...")
    except ImportError as e:
        print(f"  (Skipped - {e})")
    except Exception as e:
        print(f"  (Error: {e})")

if __name__ == "__main__":
    asyncio.run(test_ai_providers())
