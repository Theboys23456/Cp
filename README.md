# ClassPlus Token Generator API

A FastAPI backend to generate ClassPlus-style tokens using Telegram API credentials.

## Setup

1. Add `.env` file with:
```
API_ID=your_id
API_HASH=your_hash
BOT_TOKEN=your_token
```

2. Run Locally:
```bash
uvicorn main:app --reload
```

3. Deploy to Render (auto from `render.yaml`)
