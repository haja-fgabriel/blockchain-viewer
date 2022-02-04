from typing import Dict, List
import re

from cosmos_client.validators import get_validators, Validator, ValidatorUptime
from cosmos_client.validators import get_validator_blocks


def test_get_validators():
    result = get_validators()
    assert isinstance(result, List)
    for validator in result:
        assert isinstance(validator, Validator)


def test_get_validator_blocks():
    result = get_validator_blocks("")
    assert isinstance(result, List)
    for block in result:
        assert isinstance(block, Dict)
        assert isinstance(block.get("id"), int) and block.get("id") > 10 ** 6
        assert isinstance(block.get("chainid"), str) and block.get("chainid") == "cosmoshub-4"
        assert isinstance(block.get("height"), int) and block.get("height") > 9000000
        assert isinstance(block.get("proposer"), str) and re.match(r"[0-9a-fA-F]+", block.get("proposer"))
        assert isinstance(block.get("operator_address"), str)
        assert isinstance(block.get("moniker"), str)
        assert isinstance(block.get("block_hash"), str) and re.match(r"[0-9a-fA-F]+", block.get("block_hash"))
        assert isinstance(block.get("num_txs"), int)
        assert isinstance(block.get("total_num_proposer_blocks"), int)
        assert isinstance(block.get("timestamp"), str)
        assert "txs" in block
