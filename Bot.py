from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

# Замените на токен вашего бота
TOKEN = '6231361993:AAFCKT2rPnoJv2K4OXAZCpOq8KcjmFGvJjw'

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Открыть мини-приложение", web_app=WebAppInfo(url="https://mykytaa.github.io/Alchemy/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Нажмите кнопку ниже, чтобы открыть мини-приложение:", reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
