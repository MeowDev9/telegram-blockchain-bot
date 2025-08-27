# handlers/start_handler.py
from telegram import Update
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes
from menus.main_menu import main_menu
from menus.back_menu import back_menu
from services.eth_service import get_eth_price
from services.network_service import get_network_info
from utils.formatters import format_price_info, format_network_info

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to CryptoPaws Bot!\nChoose an option below 👇", reply_markup=main_menu())

# central callback query router for menu buttons (keeps logic thin)
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data

    if data == "menu":
        await q.edit_message_text("🏠 Main Menu:", reply_markup=main_menu())
        return

    if data == "price":
        eth_price = get_eth_price()
        await q.edit_message_text(f"{format_price_info(eth_price)}\n\nExample: `/price`", parse_mode="Markdown", reply_markup=back_menu())
        return

    if data == "balance":
        await q.edit_message_text("📍 Send me a wallet address:\n\nExample: `/balance 0x...`", parse_mode="Markdown", reply_markup=back_menu())
        return

    if data == "network":
        try:
            info = get_network_info()
            await q.message.reply_text(
                format_network_info(info),
                parse_mode="Markdown",
                reply_markup=back_menu()
            )
        except Exception as e:
            await q.message.reply_text(f"❌ Error: {e}", reply_markup=back_menu())
        return

    if data == "tx":
        await q.edit_message_text("🔍 Enter a transaction hash:\n\nExample: `/tx 0x...`", reply_markup=back_menu())
        return

    # if data == "tokenbalance": - handled by token conversation handler
    
    if data == "help":
        await q.edit_message_text(
            "❓ *Available Commands:*\n\n"
            "💰 `/price`\n"
            "📊 `/balance <wallet>`\n"
            "🌐 `/network`\n"
            "🔍 `/tx <hash>`\n"
            "🪙 `/tokenbalance`",
            parse_mode="Markdown",
            reply_markup=back_menu()
        )

start_handler = CommandHandler("start", start_cmd)
button_query_handler = CallbackQueryHandler(button_handler)
