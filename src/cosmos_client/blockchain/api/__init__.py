import requests


def get_blockchain_status():
    return requests.get("https://api.cosmostation.io/v1/status").text


def get_block_status(hub_id, block):
    pass
