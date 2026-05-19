import os
from openai import OpenAI, APIError
from .base import AIProvider


class OpenAICompatibleProvider(AIProvider):
    def __init__(self):
        api_key = os.getenv("AI_API_KEY")
        base_url = os.getenv("AI_BASE_URL", "https://api.openai.com/v1")
        self.model = os.getenv("AI_MODEL", "gpt-4o-mini")
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    async def chat(self, message: str, system_prompt: str | None = None) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": message})

        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return resp.choices[0].message.content
        except APIError as e:
            raise RuntimeError(f"AI provider error: {e}")
