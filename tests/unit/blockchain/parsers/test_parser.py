import json
from typing import Dict, List

from cosmos_client.blockchain.models import TokenStatus

from cosmos_client.blockchain.parsers import BlockchainStatusJSONParser, BlockchainStatus
from cosmos_client.blockchain.parsers.json import TokenStatusJSONParser


def parse_status(input):
    return json.loads(input)


def related_fields_equal(parsed_status: List[Dict], result: List[TokenStatus]):
    for token_dict, token_instance in zip(parsed_status, result):
        if token_dict.get("denom") != token_instance.denom or token_dict.get("amount") != token_instance.amount:
            return False
    return True


def fields_equal(parsed_status: Dict, result: BlockchainStatus):
    return (
        parsed_status.get("chain_id") == result.chain_id
        and parsed_status.get("block_height") == result.block_height
        and parsed_status.get("block_time") == result.block_time
        and parsed_status.get("total_txs_num") == result.total_txs_num
        and parsed_status.get("total_validator_num") == result.total_validator_num
        and parsed_status.get("unjailed_validator_num") == result.unjailed_validator_num
        and parsed_status.get("jailed_validator_num") == result.jailed_validator_num
        and parsed_status.get("bonded_tokens") == result.bonded_tokens
        and parsed_status.get("not_bonded_tokens") == result.not_bonded_tokens
        and parsed_status.get("inflation") == result.inflation
        and parsed_status.get("timestamp") == result.timestamp
        and related_fields_equal(parsed_status.get("total_supply_tokens").get("supply"), result.total_supply_tokens)
        and related_fields_equal(
            parsed_status.get("total_circulating_tokens").get("supply"), result.total_circulating_tokens
        )
    )


def test_blockchain_status_parser(sample_blockchain_status):
    parsed_status = parse_status(sample_blockchain_status)
    parser = BlockchainStatusJSONParser()
    result = parser.parse(sample_blockchain_status)
    assert isinstance(result, BlockchainStatus)
    assert fields_equal(parsed_status, result)


def test_token_status_parser():
    sample_status = """{
        "denom": "uatom",
        "amount": "886976236202.923011039302482497"
    }"""
    parsed_status = parse_status(sample_status)
    parser = TokenStatusJSONParser()
    result = parser.parse(sample_status)
    assert parsed_status.get("denom") == result.denom
    assert parsed_status.get("amount") == result.amount
