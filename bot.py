from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ✨ ប្តូរទៅ Bot Token របស់អ្នក
TOKEN = "8324864531:AAFJLZRRFpC2LGbfaucec31pQa99zVaeacM"

# កំណត់អត្ថបទសម្រាប់ Menu
menu_messages = {
    "info": "នេះគឺព័ត៌មានរបស់យើង។\n- ព័ត៌មាន1\n- ព័ត៌មាន2",
    "links": "នេះគឺ Links ដែលអ្នកអាចចុចបាន៖\nhttps://example.com\nhttps://example2.com",
    "contact": "ទំនាក់ទំនង:\n📞 012 345 678\n📧 email@example.com",
    "settings": "Settings មានជម្រើស៖\n1) Language\n2) Notifications\n3) Privacy"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📄 ព័ត៌មាន", callback_data='info')],
        [InlineKeyboardButton("📎 Links", callback_data='links')],
        [InlineKeyboardButton("☎️ ទំនាក់ទំនង", callback_data='contact')],
        [InlineKeyboardButton("⚙️ ការកំណត់", callback_data='settings')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("សូមជ្រើសមីនុយខាងក្រោម👇", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # ផ្ញើអត្ថបទដែលបានកំណត់សម្រាប់ Menu
    message_to_send = menu_messages.get(query.data, "មិនមានអត្ថបទសម្រាប់ Menu នេះ")
    await query.edit_message_text(message_to_send)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
