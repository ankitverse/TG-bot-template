from pyrogram import Client
from config import *

def main():
    plugins = dict(root="plugins")
    app = Client("TG-Sample-bot",
                 bot_token=BOT_TOKEN,
                 api_id=API_ID,
                 api_hash=API_HASH,
                 plugins=plugins,
                 workers=100)

    print("the bot is running successfully")
    app.run()
    


if __name__ == "__main__":
    main()
    