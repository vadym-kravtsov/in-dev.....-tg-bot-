import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
try:
    ADMIN_ID = int(os.getenv('USER_ID'))
except (ValueError, TypeError):
    print("Error user_id (ADMIN_ID)")
    ADMIN_ID = None

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found")


