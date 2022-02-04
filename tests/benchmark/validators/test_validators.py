import re
from typing import List, Dict

import pytest

from cosmos_client.validators import get_validators, Validator, ValidatorUptime, get_validator_blocks


def test_get_validators():
    result = get_validators()
    assert isinstance(result, List)
    for validator in result:
        assert isinstance(validator, Validator)


@pytest.mark.parametrize(
    ("validator_id", "limit", "offset"),
    [
        ("cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf", 45, 0),
        ("cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf", 100, 0),
        ("cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf", 10000, 0),
    ],
)
def test_get_validator_blocks(validator_id, limit, offset):
    result = get_validator_blocks(validator_id, limit, offset)
    assert isinstance(result, List)
    assert len(result) <= limit
    for block in result:
        assert isinstance(block, Dict)
        assert isinstance(block.get("id"), int) and block.get("id") > 10 ** 6
        assert isinstance(block.get("chainid"), str) and block.get("chainid") == "cosmoshub-4"
        assert isinstance(block.get("height"), int) and block.get("height") > 9000000
        assert isinstance(block.get("proposer"), str) and re.match(r"[0-9a-fA-F]+", block.get("proposer"))
        assert isinstance(block.get("operator_address"), str) and block.get("operator_address") == validator_id
        assert isinstance(block.get("moniker"), str)
        assert isinstance(block.get("block_hash"), str) and re.match(r"[0-9a-fA-F]+", block.get("block_hash"))
        assert isinstance(block.get("num_txs"), int) and block.get("num_txs") >= 0
        assert isinstance(block.get("total_num_proposer_blocks"), int)
        assert isinstance(block.get("timestamp"), str)
        assert "txs" in block
