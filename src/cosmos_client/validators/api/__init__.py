import requests


def get_validators():
    return requests.get("https://api.cosmostation.io/v1/staking/validators").text


def get_validator_blocks(validator_id, limit=45, from_=0):
    return requests.get(f"https://api.cosmostation.io/v1/blocks/{validator_id}?limit={limit}&from={from_}").text
