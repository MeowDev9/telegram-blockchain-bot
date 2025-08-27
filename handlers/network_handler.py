# handlers/network_handler.py
from telegram.ext import CommandHandler
from services.network_service import get_network_info
from utils.formatters import format_network_info
from menus.back_menu import back_menu

async def network_cmd(update, context):
    try:
        info = get_network_info()
        await update.message.reply_text(
            format_network_info(info),
            parse_mode="Markdown",
            reply_markup=back_menu()
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error fetching network info:\n`{e}`", parse_mode="Markdown", reply_markup=back_menu())

network_handler = CommandHandler("network", network_cmd)

network_handler = CommandHandler("network", network_cmd)
