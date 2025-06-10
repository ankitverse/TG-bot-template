import os 
import dotenv
dotenv.load_dotenv()

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
OWNER = int(os.environ.get("OWNER", ""))
MONGO_DB_URI = os.environ.get("MOGNO_DB_URI","")