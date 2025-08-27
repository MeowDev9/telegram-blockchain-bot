# handlers/tx_handler.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler
from services.tx_service import get_tx_info
from utils.formatters import format_tx_info
from menus.back_menu import back_menu

async def tx_cmd(update, context):
    if len(context.args) != 1:
        await update.message.reply_text("⚠️ Usage: /tx <transaction_hash>", reply_markup=back_menu())
        return

    tx_hash = context.args[0]
    try:
        info = get_tx_info(tx_hash)

        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 View on Etherscan", url=info["etherscan"])],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")]
        ])

        await update.message.reply_text(
            format_tx_info(info),
            parse_mode="Markdown",
            reply_markup=kb
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error fetching transaction: {e}", reply_markup=back_menu())

tx_handler = CommandHandler("tx", tx_cmd)
