from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def back_menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")]])
