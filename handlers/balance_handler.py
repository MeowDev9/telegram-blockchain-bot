# handlers/balance_handler.py
from telegram.ext import CommandHandler
from config.settings import w3
from menus.back_menu import back_menu
from utils.formatters import format_eth_balance, shorten_address

async def balance_cmd(update, context):
    try:
        # Get wallet from args
        wallet = context.args[0]

        # Fetch ETH balance
        balance = w3.eth.get_balance(wallet)

        # Format nicely
        eth_balance = format_eth_balance(balance)
        short_wallet = shorten_address(wallet)

        # Send response
        await update.message.reply_text(
            f"📊 Balance of {short_wallet}:\n{eth_balance}",
            reply_markup=back_menu()
        )

    except IndexError:
        await update.message.reply_text(
            "⚠️ Usage: /balance <wallet_address>",
            reply_markup=back_menu()
        )

    except Exception as e:
        await update.message.reply_text(
            f"❌ Error: {e}",
            reply_markup=back_menu()
        )

# Register command
balance_handler = CommandHandler("balance", balance_cmd)
