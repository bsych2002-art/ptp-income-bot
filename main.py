import os
from telegram.ext import Application, CommandHandler

from handlers import start, create_order, list_orders

TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("create", create_order))
    app.add_handler(CommandHandler("orders", list_orders))

    print("BOT STARTED")
    app.run_polling()

if __name__ == "__main__":
    main()