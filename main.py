from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ ربات سیگنال فعال است.\n\n"
        "جفت‌های معاملاتی:\n"
        "XAU/USD\n"
        "US30 (Dow Jones)\n"
        "Brent Oil"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
