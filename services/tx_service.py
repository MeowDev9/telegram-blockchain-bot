# services/tx_service.py
from web3.exceptions import TransactionNotFound
from config.settings import w3
from utils.constants import ETHERSCAN_NETWORKS

def get_tx_info(tx_hash):
    tx = w3.eth.get_transaction(tx_hash)
    try:
        receipt = w3.eth.get_transaction_receipt(tx_hash)
    except TransactionNotFound:
        receipt = None

    latest = w3.eth.block_number
    if receipt and receipt.blockNumber is not None:
        confirmations = latest - receipt.blockNumber + 1
    else:
        confirmations = 0

    gas_used = receipt.gasUsed if receipt else tx["gas"]
    gas_price_gwei = w3.from_wei(tx["gasPrice"], "gwei") if "gasPrice" in tx else None

    status = "Pending" if receipt is None else ("Success" if receipt.status == 1 else "Failed")

    chain_id = w3.eth.chain_id
    base = ETHERSCAN_NETWORKS.get(chain_id, "https://etherscan.io/tx/{}")
    etherscan_url = base.format(tx_hash)

    return {
        "hash": tx_hash,
        "from": tx["from"],
        "to": tx.get("to"),
        "value_eth": w3.from_wei(tx["value"], "ether"),
        "gas_used": gas_used,
        "gas_price_gwei": gas_price_gwei,
        "block": tx.get("blockNumber"),
        "status": status,
        "confirmations": confirmations,
        "etherscan": etherscan_url,
    }
