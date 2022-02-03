import json
from typing import Any, Dict

from ..models import Validator, ValidatorUptime


class ValidatorUptimeJSONParser:
    def from_dict(self, parsed_input: Dict[str, Any]) -> ValidatorUptime:
        return ValidatorUptime(**parsed_input)

    def parse(self, input: str) -> ValidatorUptime:
        parsed_input = json.loads(input)
        return self.from_dict(parsed_input)


class ValidatorJSONParser:
    def __init__(self) -> None:
        self.__validator_uptime_parser = ValidatorUptimeJSONParser()

    def from_list(self, parsed_input: Dict[str, Any]) -> Validator:
        return [
            *map(
                lambda parsed_input: Validator(
                    rank=parsed_input.get("rank"),
                    account_address=parsed_input.get("account_address"),
                    operator_address=parsed_input.get("operator_address"),
                    consensus_pubkey=parsed_input.get("consensus_pubkey"),
                    jailed=parsed_input.get("jailed"),
                    status=parsed_input.get("status"),
                    tokens=parsed_input.get("tokens"),
                    delegator_shares=parsed_input.get("delegator_shares"),
                    moniker=parsed_input.get("moniker"),  # Monica, but misspelled
                    identity=parsed_input.get("identity"),
                    website=parsed_input.get("website"),
                    details=parsed_input.get("details"),
                    unbonding_height=parsed_input.get("unbonding_height"),
                    unbonding_time=parsed_input.get("unbonding_time"),
                    rate=parsed_input.get("rate"),
                    max_rate=parsed_input.get("max_rate"),
                    max_change_rate=parsed_input.get("max_change_rate"),
                    update_time=parsed_input.get("update_time"),
                    uptime=self.__validator_uptime_parser.from_dict(parsed_input.get("uptime")),
                    min_self_delegation=parsed_input.get("min_self_delegation"),
                    keybase_url=parsed_input.get("keybase_url"),
                ),
                parsed_input,
            )
        ]

    def parse(self, input: str) -> Validator:
        parsed_input = json.loads(input)
        return self.from_list(parsed_input)
