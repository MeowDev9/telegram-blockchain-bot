# handlers/token_handler.py
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from services.token_service import get_token_balance
from menus.back_menu import back_menu
from menus.main_menu import main_menu
from utils.constants import TOKEN_MAP
from utils.formatters import shorten_address, format_token_balance_simple

ASK_WALLET, ASK_TOKEN, ASK_CUSTOM = range(3)


def token_keyboard():
    """Token selection keyboard (symbols + Other)."""
    keys = [
        [InlineKeyboardButton(s, callback_data=f"tb:{s}")]
        for s in TOKEN_MAP.keys()
    ]
    keys.append([InlineKeyboardButton("📦 Other (paste contract)", callback_data="tb:other")])
    keys.append([InlineKeyboardButton("⬅️ Cancel", callback_data="tb:cancel")])
    return InlineKeyboardMarkup(keys)


# STEP 1 – Start
async def tb_start_command(update, context):
    await update.message.reply_text(
        "📍 Send the wallet address you want to check (0x...):",
        reply_markup=back_menu()
    )
    return ASK_WALLET


async def tb_start_button(update, context):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(
        "📍 Send the wallet address you want to check (0x...):",
        reply_markup=back_menu()
    )
    return ASK_WALLET


# STEP 2 – Wallet
async def tb_wallet_received(update, context):
    from config.settings import w3
    wallet = (update.message.text or "").strip()

    if not w3.is_address(wallet):
        await update.message.reply_text("❌ Invalid wallet address. Try again.", reply_markup=back_menu())
        return ASK_WALLET

    wallet = w3.to_checksum_address(wallet)
    context.user_data["tb_wallet"] = wallet

    await update.message.reply_text(
        f"✅ Wallet saved: `{shorten_address(wallet)}`\n\nNow choose a token:",
        parse_mode="Markdown",
        reply_markup=token_keyboard()
    )
    return ASK_TOKEN


# STEP 3 – Token chosen
async def tb_token_chosen(update, context):
    q = update.callback_query
    await q.answer()
    data = q.data.split(":", 1)[1]

    if data == "other":
        await q.edit_message_text("Paste the token contract address (0x...):", reply_markup=back_menu())
        return ASK_CUSTOM

    wallet = context.user_data.get("tb_wallet")
    if not wallet:
        await q.edit_message_text("⚠️ Wallet missing, please start again.", reply_markup=back_menu())
        return ConversationHandler.END

    try:
        result = get_token_balance(wallet, data)
        token_menu = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 Token on Etherscan", url=f"https://etherscan.io/token/{result['address']}")],
            [InlineKeyboardButton("🔗 Wallet on Etherscan", url=f"https://etherscan.io/address/{wallet}")],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")]
        ])
        await q.edit_message_text(
            f"💰 *Token Balance*\n"
            f"- Wallet: `{shorten_address(wallet)}`\n"
            f"- Token: {result['symbol']}\n"
            f"- Balance: {format_token_balance_simple(result['balance'], result['symbol'])}",
            parse_mode="Markdown",
            reply_markup=token_menu
        )
    except Exception as e:
        await q.edit_message_text(f"❌ Error: {e}", reply_markup=back_menu())

    return ConversationHandler.END


# STEP 4 – Custom contract entered
async def tb_custom_received(update, context):
    from config.settings import w3
    token_addr = (update.message.text or "").strip()

    if not w3.is_address(token_addr):
        await update.message.reply_text("❌ Invalid token contract address. Try again.", reply_markup=back_menu())
        return ASK_CUSTOM

    wallet = context.user_data.get("tb_wallet")
    if not wallet:
        await update.message.reply_text("⚠️ Wallet missing, start again.", reply_markup=back_menu())
        return ConversationHandler.END

    try:
        result = get_token_balance(wallet, token_addr)
        menu = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 Token on Etherscan", url=f"https://etherscan.io/token/{result['address']}")],
            [InlineKeyboardButton("🔗 Wallet on Etherscan", url=f"https://etherscan.io/address/{wallet}")],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")]
        ])
        await update.message.reply_text(
            f"💰 *Token Balance*\n"
            f"- Wallet: `{shorten_address(wallet)}`\n"
            f"- Token: {result['symbol']}\n"
            f"- Balance: {format_token_balance_simple(result['balance'], result['symbol'])}",
            parse_mode="Markdown",
            reply_markup=menu
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}", reply_markup=back_menu())

    return ConversationHandler.END


# STEP 5 – Cancel
async def tb_cancel(update, context):
    if update.callback_query:
        q = update.callback_query
        await q.answer()
        await q.edit_message_text("Cancelled. Back to menu:", reply_markup=main_menu())
    else:
        await update.message.reply_text("Cancelled. Back to menu.")
    return ConversationHandler.END


# Export conversation handler
token_conv = ConversationHandler(
    entry_points=[
        CommandHandler("tokenbalance", tb_start_command),
        CallbackQueryHandler(tb_start_button, pattern="^tokenbalance$")
    ],
    states={
        ASK_WALLET: [MessageHandler(filters.TEXT & ~filters.COMMAND, tb_wallet_received)],
        ASK_TOKEN:  [CallbackQueryHandler(tb_token_chosen, pattern="^tb:")],
        ASK_CUSTOM: [MessageHandler(filters.TEXT & ~filters.COMMAND, tb_custom_received)],
    },
    fallbacks=[CommandHandler("cancel", tb_cancel)],
)
