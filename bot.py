from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات خود را اینجا قرار دهید
TOKEN = "6414210268:AAEL-RZiABoMzS_QY922hOQnpXcam9OgiF0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من یک ربات ساده هستم. می‌توانید با من چت کنید!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()
    
    if message_text == "سلام":
        await update.message.reply_text("علیک سلام")
    elif message_text == "کجایی":
        await update.message.reply_text("خانه هستم")

def main():
    # ایجاد برنامه
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلرها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # شروع ربات
    print("ربات در حال اجراست...")
    application.run_polling()

if __name__ == "__main__":
    main() 
