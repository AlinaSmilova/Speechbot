
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from voice import voice_handler
from voice import text_to_file

async def start(update, context):
    await update.message.reply_text(f'Please, to start using this bot 👉 /hello')

async def hello(update, context):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, I am a text_to_speech and speech_to_text bot. So talk to me or write. Whatever... ')

async def reply(update, context):
    file_name = text_to_file(update.message.text)
    await update.message.reply_voice(voice=open(file_name, "rb"))
    await update.message.reply_text("Ta-dam")
    await update.message.reply_text("You typed 🧐:" + (update.message.text))   
    
app = ApplicationBuilder().token("5950882810:AAHVuW9ZlUrQ63cFfvapHK_iV63QXLm3ksY").build()
app.add_handler(MessageHandler(filters.VOICE & ~filters.COMMAND, voice_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))

app.run_polling()    


