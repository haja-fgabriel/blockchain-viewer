import requests


def get_tokens(token_id):
    return requests.get(f"https://api-utility.cosmostation.io/v1//market/price?id={token_id}").text
