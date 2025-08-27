# services/network_service.py
from config.settings import w3

def get_network_info():
    latest_block = w3.eth.block_number
    chain_id = w3.eth.chain_id
    try:
        peer_count = w3.net.peer_count
    except Exception:
        peer_count = "Unavailable"
    return {"chain_id": chain_id, "latest_block": latest_block, "peer_count": peer_count}
