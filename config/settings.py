import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found")