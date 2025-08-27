# services/token_service.py
from config.settings import w3, ERC20_ABI
from utils.constants import TOKEN_MAP

def resolve_token_address(input_token):
    # if symbol -> map else treat as address
    if input_token.upper() in TOKEN_MAP:
        return TOKEN_MAP[input_token.upper()]
    if w3.is_address(input_token):
        return w3.to_checksum_address(input_token)
    raise ValueError("Invalid token symbol or address")

def get_token_balance(wallet, token_input):
    token_address = resolve_token_address(token_input)
    contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
    decimals = contract.functions.decimals().call()
    symbol = contract.functions.symbol().call()
    raw = contract.functions.balanceOf(wallet).call()
    adjusted = raw / (10 ** decimals)
    return {"symbol": symbol, "address": token_address, "balance": adjusted}
