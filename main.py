import os
from fastapi import FastAPI, Query
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("21567814"))
API_HASH = os.getenv("cd7dc5431d449fd795683c550d7bfb7e")
BOT_TOKEN = os.getenv("7864597080:AAHfJO_1bXx7i8cPVRjDhG1-hwF71EWSFL4")

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
