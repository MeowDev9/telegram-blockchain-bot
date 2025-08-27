# CryptoPaws - Telegram Blockchain Bot

A Python-based Telegram bot that integrates with Ethereum blockchain to provide real-time price, wallet, transaction, and token data.

##  Features

- 💰 **ETH Price**: Get real-time Ethereum price from CoinGecko
- 📊 **Wallet Balance**: Check ETH balance for any wallet address
- 🌐 **Network Info**: View Ethereum network details (Chain ID, latest block, peer count)
- 🔍 **Transaction Lookup**: Get detailed transaction information with Etherscan links
- 🪙 **Token Balance**: Check ERC20 token balances (USDT, USDC, DAI, LINK, UNI, MKR)
- 📱 **Interactive Menus**: User-friendly button-based navigation

##  Project Structure

```
telegram-blockchain-bot/
├── config/
│   └── settings.py          # Web3 and configuration setup
├── handlers/
│   ├── balance_handler.py   # ETH balance functionality
│   ├── network_handler.py   # Network information
│   ├── price_handler.py     # ETH price tracking
│   ├── start_handler.py     # Bot start and button handling
│   ├── token_handler.py     # ERC20 token interactions
│   └── tx_handler.py        # Transaction lookup
├── menus/
│   ├── back_menu.py         # Back button menu
│   └── main_menu.py         # Main navigation menu
├── services/
│   ├── eth_service.py       # Ethereum price service
│   ├── network_service.py   # Network information service
│   ├── token_service.py     # Token balance service
│   └── tx_service.py        # Transaction lookup service
├── utils/
│   ├── constants.py         # Token mappings and constants
│   └── formatters.py        # Data formatting utilities
├── erc20_abi.json          # ERC20 contract ABI
├── main.py                 # Bot entry point
└── requirements.txt        # Python dependencies
```

##  Setup & Installation

### Prerequisites
- Python 3.8+
- Telegram Bot Token (from @BotFather)
- Ethereum RPC endpoint (Infura, Alchemy, etc.)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MeowDev9/telegram-blockchain-bot.git
   cd telegram-blockchain-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Copy the example environment file and add your credentials:
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` with your actual values:
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token_here
   ETH_RPC=your_ethereum_rpc_endpoint_here
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

## 🔧 Configuration

### Environment Variables
- `TELEGRAM_TOKEN`: Your Telegram bot token from BotFather
- `ETH_RPC`: Ethereum RPC endpoint URL

### Supported Networks
- Ethereum Mainnet
- Goerli Testnet
- Sepolia Testnet

### Supported Tokens
- USDT (Tether)
- USDC (USD Coin)
- DAI (Dai Stablecoin)
- LINK (Chainlink)
- UNI (Uniswap)
- MKR (Maker)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Built With

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot API wrapper
- [web3.py](https://github.com/ethereum/web3.py) - Ethereum interaction library
- [requests](https://github.com/psf/requests) - HTTP library for API calls

##  Support

For questions, suggestions, or bug reports, please open an issue in this repository

---

⭐ **Star this repo if you found it helpful!**
