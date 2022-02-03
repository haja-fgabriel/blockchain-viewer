import json
from typing import Any, Dict, List

from cosmos_client.validators.models import Validator, ValidatorUptime
from cosmos_client.validators.parsers.json import ValidatorJSONParser, ValidatorUptimeJSONParser


def parse_sample(sample):
    return json.loads(sample)


def fields_equal(validator: Validator, dict_validator: Dict[str, Any]):
    return (
        validator.rank == dict_validator.get("rank")
        and validator.account_address == dict_validator.get("account_address")
        and validator.operator_address == dict_validator.get("operator_address")
        and validator.consensus_pubkey == dict_validator.get("consensus_pubkey")
        and validator.jailed == dict_validator.get("jailed")
        and validator.status == dict_validator.get("status")
        and validator.tokens == dict_validator.get("tokens")
        and validator.delegator_shares == dict_validator.get("delegator_shares")
        and validator.moniker == dict_validator.get("moniker")
        and validator.identity == dict_validator.get("identity")
        and validator.website == dict_validator.get("website")
        and validator.details == dict_validator.get("details")
        and validator.unbonding_height == dict_validator.get("unbonding_height")
        and validator.unbonding_time == dict_validator.get("unbonding_time")
        and validator.rate == dict_validator.get("rate")
        and validator.max_rate == dict_validator.get("max_rate")
        and validator.max_change_rate == dict_validator.get("max_change_rate")
        and validator.update_time == dict_validator.get("update_time")
        and validator.min_self_delegation == dict_validator.get("min_self_delegation")
        and validator.keybase_url == dict_validator.get("keybase_url")
        and validator.uptime.address == dict_validator.get("uptime").get("address")
        and validator.uptime.missed_blocks == dict_validator.get("uptime").get("missed_blocks")
        and validator.uptime.over_blocks == dict_validator.get("uptime").get("over_blocks")
    )


def test_validator_parser(sample_validator_list):
    parser = ValidatorJSONParser()
    parsed_sample = parse_sample(sample_validator_list)
    result = parser.parse(sample_validator_list)
    assert isinstance(result, List)
    for validator, dict_validator in zip(result, parsed_sample):
        assert isinstance(validator, Validator)
        assert fields_equal(validator, dict_validator)


def test_validator_uptime_parser():
    sample = """{
        "address": "83F47D7747B0F633A6BA0DF49B7DCF61F90AA1B0",
        "missed_blocks": 1,
        "over_blocks": 100
    }"""
    parsed_sample = parse_sample(sample)
    parser = ValidatorUptimeJSONParser()
    result = parser.parse(sample)
    assert isinstance(result, ValidatorUptime)
    assert result.address == parsed_sample.get("address")
    assert result.missed_blocks == parsed_sample.get("missed_blocks")
    assert result.over_blocks == parsed_sample.get("over_blocks")
