from pyrogram import Client , filters 


#echo bot logic 
# @Client.on_message(filters.private & filters.incoming)
# def echo(bot,msg):
#     txt = msg.text
#     msg.reply_text(txt)

@Client.on_message(filters.command("start") & filters.private)
def start(bot,msg):
    bot.send_message(msg.from_user.id,
                     "This is Start command")
    