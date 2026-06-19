from telegram import Update
from telegram.ext import ContextTypes
from storage import add_order, get_orders


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 P2P бот работает!\n"
        "Команды:\n"
        "/create buy 100\n"
        "/orders"
    )


async def create_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        side = context.args[0]
        amount = context.args[1]

        add_order(update.effective_user.id, side, amount)

        await update.message.reply_text(f"✅ Заявка: {side} {amount}")
    except:
        await update.message.reply_text("❌ Используй: /create buy 100")


async def list_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    orders = get_orders()

    if not orders:
        await update.message.reply_text("📭 Нет заявок")
        return

    text = "📌 Заявки:\n"
    for o in orders:
        text += f"- {o['side']} {o['amount']} (user {o['user_id']})\n"

    await update.message.reply_text(text)