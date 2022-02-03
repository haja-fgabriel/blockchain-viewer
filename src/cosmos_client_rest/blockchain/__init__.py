from .parsers import BlockchainStatusJSONParser
from .api import get_blockchain_status as api_get_blockchain_status
from .models import *


def get_blockchain_status():
    parser = BlockchainStatusJSONParser()
    return parser.parse(api_get_blockchain_status())
