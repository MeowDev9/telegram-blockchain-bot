from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💰 ETH Price", callback_data="price")],
        [InlineKeyboardButton("📊 Check Balance", callback_data="balance")],
        [InlineKeyboardButton("🌐 Network Info", callback_data="network")],
        [InlineKeyboardButton("🔍 Transaction Lookup", callback_data="tx")],
        [InlineKeyboardButton("🪙 Token Balance", callback_data="tokenbalance")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ])
