# utils/formatters.py
from decimal import Decimal

def format_eth_balance(balance_wei: int) -> str:
    """Format ETH balance from Wei to ETH with 4 decimals"""
    eth = Decimal(balance_wei) / Decimal(10**18)
    return f"{eth:.4f} ETH"

def format_token_balance(balance: int, decimals: int, symbol: str) -> str:
    """Format ERC20 balance with proper decimals"""
    token = Decimal(balance) / Decimal(10**decimals)
    return f"{token:.4f} {symbol}"

def format_token_balance_simple(balance: float, symbol: str) -> str:
    """Format already-adjusted ERC20 balance"""
    return f"{balance:.4f} {symbol}"

def shorten_address(address: str) -> str:
    """Shorten Ethereum address for display"""
    if not address:
        return "N/A"
    return f"{address[:6]}...{address[-4:]}"

def format_usd(price: float) -> str:
    """Format price in USD"""
    return f"${price:,.2f}"

def format_tx_link(tx_hash: str, etherscan_base: str) -> str:
    """Return clickable Etherscan link"""
    return f"<a href='{etherscan_base}/tx/{tx_hash}'>View on Etherscan</a>"

# utils/formatters.py

def format_tx_info(info: dict) -> str:
    """Format transaction info nicely for Telegram messages."""
    return (
        f"🔍 *Transaction Info*\n"
        f"- Hash: `{info['hash']}`\n"
        f"- From: `{info['from']}`\n"
        f"- To: `{info['to']}`\n"
        f"- Value: {float(info['value_eth']):.4f} ETH\n"
        f"- Gas Used: {info['gas_used']}\n"
        f"- Gas Price: {info['gas_price_gwei']} gwei\n"
        f"- Block: {info['block']}\n"
        f"- Status: {info['status']}\n"
        f"- Confirmations: {info['confirmations']}"
    )

def format_price_info(price: float) -> str:
    """Format ETH price info for Telegram messages."""
    return f"💰 Current ETH Price: {format_usd(price)}"

def format_network_info(info: dict) -> str:
    """Format network info for Telegram messages."""
    return (
        f"🌐 *Ethereum Network Info*\n"
        f"- Chain ID: `{info['chain_id']}`\n"
        f"- Latest Block: `{info['latest_block']}`\n"
        f"- Peer Count: `{info['peer_count']}`"
    )
