import json
from typing import Any, Dict
from .parsers import BlockchainStatusJSONParser
from .api import get_blockchain_status as api_get_blockchain_status, get_block_status as api_get_block_status
from .models import *


def get_blockchain_status():
    parser = BlockchainStatusJSONParser()
    return parser.parse(api_get_blockchain_status())


def get_block_status(hub: str, block: int) -> List[Dict[str, Any]]:
    return json.loads(api_get_block_status(hub, block))
