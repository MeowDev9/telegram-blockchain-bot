# services/eth_service.py
import requests
from config.settings import w3

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    r = requests.get(url, timeout=8)
    r.raise_for_status()
    return r.json()["ethereum"]["usd"]

def get_eth_balance(address):
    balance_wei = w3.eth.get_balance(address)
    return w3.from_wei(balance_wei, "ether")
