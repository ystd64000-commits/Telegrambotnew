import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("TOKEN", "YOUR_BOT_TOKEN_HERE")

# Custom messages for items
menu_messages = {
    "item1": "អត្ថបទ item 1",
    "item2": "អត្ថបទ item 2",
    "item3": "អត្ថបទ item 3",
    "item4": "អត្ថបទ item 4",
    "item5": "អត្ថបទ item 5",
    "item6": "អត្ថបទ item 6",
    "item7": "អត្ថបទ item 7",
}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 អានរឿង", callback_data='story_main')],
        [InlineKeyboardButton("📎 Links", callback_data='links')],
        [InlineKeyboardButton("☎️ ទំនាក់ទំនង", callback_data='contact')],
        [InlineKeyboardButton("⚙️ ការកំណត់", callback_data='settings')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("សូមជ្រើសមីនុយខាងក្រោម👇", reply_markup=reply_markup)

# Generate 7-item submenu dynamically
def generate_7_item_keyboard(back_data):
    keyboard = []
    for i in range(1, 8):
        keyboard.append([InlineKeyboardButton(str(i), callback_data=f'item{i}')])
    keyboard.append([InlineKeyboardButton("⬅️ ត្រឡប់ក្រោយ", callback_data=back_data)])
    return InlineKeyboardMarkup(keyboard)

# Handle button clicks
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Main menu → អានរឿង
    if query.data == "story_main":
        keyboard = [
            [InlineKeyboardButton("រឿងអ្នកមាន", callback_data='story_custom')],
            [InlineKeyboardButton("រឿង2", callback_data='story2')],
            [InlineKeyboardButton("រឿង3", callback_data='story3')],
            [InlineKeyboardButton("រឿង4", callback_data='story4')],
            [InlineKeyboardButton("រឿង5", callback_data='story5')],
            [InlineKeyboardButton("⬅️ ត្រឡប់ក្រោយ", callback_data='back_main')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("សូមជ្រើសរើសរឿងដែលអ្នកចង់អាន👇", reply_markup=reply_markup)
        return

    # Submenu រឿងអ្នកមាន, រឿង2, រឿង3, រឿង4, រឿង5 → 7 items
    if query.data in ["story_custom","story2","story3","story4","story5"]:
        reply_markup = generate_7_item_keyboard(back_data='story_main')
        await query.edit_message_text(f"សូមជ្រើសរើសអត្ថបទសម្រាប់ {query.data}👇", reply_markup=reply_markup)
        return

    # Back to main menu
    if query.data == "back_main":
        await start(update, context)
        return

    # Send message for item1-item7
    message_to_send = menu_messages.get(query.data, f"នេះគឺ {query.data}")
    await query.edit_message_text(message_to_send)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
