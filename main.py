import os
from fastapi import FastAPI, Query
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ClassPlus Token API Active"}

@app.get("/token")
async def generate_token(phone: str = Query(..., description="Telegram Phone Number")):
    try:
        async with TelegramClient(f"sessions/{phone}", API_ID, API_HASH) as client:
            me = await client.get_me()
            return {
                "phone": phone,
                "user_id": me.id,
                "token": "FAKE_CLASSPLUS_TOKEN_123456"  # Replace with real logic
            }
    except Exception as e:
        return {"error": str(e)}
