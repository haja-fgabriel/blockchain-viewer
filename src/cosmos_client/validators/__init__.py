import json
from typing import Dict, List, Any

from cosmos_client.validators.parsers.json import ValidatorJSONParser
from .api import get_validators as api_get_validators, get_validator_blocks as api_get_validator_blocks
from .models import *


def get_validators() -> List[Validator]:
    parser = ValidatorJSONParser()
    return parser.parse(api_get_validators())


def get_validator_blocks(validator_id, limit=45, from_=0) -> List[Dict[str, Any]]:
    return json.loads(api_get_validator_blocks(validator_id, limit, from_))
