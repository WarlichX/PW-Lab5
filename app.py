import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from flask import Flask, request

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

app = Flask(__name__)
application = ApplicationBuilder().token('6046575890:AAHjc6Fn_zBn5GJUbzTx75Hg0FXM5QNwzEM').build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot. Give Alex a good mark!")

if __name__ == '__main__':
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    @app.route('/webhook', methods=['POST'])
    def webhook():
        update = Update.de_json(request.get_json(force=True), application.bot)
        application.updater.dispatcher.process_update(update)
        return 'OK'

    application.run_polling()
