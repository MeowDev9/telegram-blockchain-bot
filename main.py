from telegram.ext import Application
import os
from dotenv import load_dotenv

# Import handlers
from handlers.start_handler import start_handler, button_query_handler
from handlers.price_handler import price_handler
from handlers.balance_handler import balance_handler
from handlers.network_handler import network_handler
from handlers.tx_handler import tx_handler
from handlers.token_handler import token_conv

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    """Main function to set up and run the bot."""
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add all handlers
    app.add_handler(start_handler)
    app.add_handler(token_conv)  # Conversation handler MUST come before general button handler
    app.add_handler(button_query_handler)
    app.add_handler(price_handler)
    app.add_handler(balance_handler)
    app.add_handler(network_handler)
    app.add_handler(tx_handler)

    print("🤖 CryptoPaws Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
