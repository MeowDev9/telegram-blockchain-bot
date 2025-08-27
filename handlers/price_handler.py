# handlers/price_handler.py
from telegram.ext import CommandHandler
from services.eth_service import get_eth_price
from utils.formatters import format_price_info
from menus.back_menu import back_menu

async def price_cmd(update, context):
    price = get_eth_price()
    await update.message.reply_text(format_price_info(price), reply_markup=back_menu())

price_handler = CommandHandler("price", price_cmd)
