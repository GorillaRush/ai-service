# Custom AI Service

OpenAI-compatible AI service deployable on Railway in 2 minutes.

## Deploy

1. Push this repo to GitHub
2. On [Railway](https://railway.com), click **New Project** → **Deploy from GitHub repo**
3. Select this repo
4. Add these environment variables (Railway dashboard → Variables):

| Variable | Value |
|---|---|
| `AI_API_KEY` | Your API key (get a free one at [Groq](https://console.groq.com)) |
| `AI_BASE_URL` | `https://api.groq.com/openai/v1` |
| `AI_MODEL` | `llama-3.3-70b-versatile` |

That's it. Railway detects Python, installs deps, and starts the server.

## Use it

```bash
curl https://your-app.railway.app/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
```

## Free providers

| Provider | Base URL | Free? |
|---|---|---|
| [Groq](https://console.groq.com) | `https://api.groq.com/openai/v1` | Yes (30 req/min) |
| [OpenAI](https://platform.openai.com) | `https://api.openai.com/v1` | Paid |
| [Together](https://together.ai) | `https://api.together.xyz/v1` | Paid |
| [OpenRouter](https://openrouter.ai) | `https://openrouter.ai/api/v1` | Free tier |

## Endpoints

- `GET /health` — health check
- `POST /chat` — `{"message": "...", "system_prompt": "..."}`
