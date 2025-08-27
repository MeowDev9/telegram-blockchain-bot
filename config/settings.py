# config/settings.py
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ETH_RPC = os.getenv("ETH_RPC", "https://rpc.ankr.com/eth")  # fallback
w3 = Web3(Web3.HTTPProvider(ETH_RPC))

# load ERC20 ABI from project root file erc20_abi.json
ABI_PATH = Path(__file__).parent.parent / "erc20_abi.json"
ERC20_ABI = json.load(open(ABI_PATH))
