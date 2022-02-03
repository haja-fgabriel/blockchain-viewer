import requests


def get_validators():
    return requests.get(" https://api.cosmostation.io/v1/staking/validators").text
