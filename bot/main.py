from telegram.ext import Application, CommandHandler
from bot.handlers import start, create_order, list_orders
from bot.config import TOKEN

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("create", create_order))
    app.add_handler(CommandHandler("orders", list_orders))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()