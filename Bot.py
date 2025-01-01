from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен вашего бота
TOKEN = '6231361993:AAFCKT2rPnoJv2K4OXAZCpOq8KcjmFGvJjw'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть мини-приложение", web_app=WebAppInfo(url="https://mykytaa.github.io/Alchemy/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажмите кнопку ниже, чтобы открыть мини-приложение:", reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__':
    main()
