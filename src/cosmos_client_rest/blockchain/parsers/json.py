from datetime import datetime
import json
from typing import Dict, Any, List

from cosmos_client_rest.blockchain import BlockchainStatus, TokenStatus


class TokenStatusJSONParser:
    def from_dict(self, parsed_input: Dict[str, Any]):
        return TokenStatus(**parsed_input)

    def parse(self, input: str) -> TokenStatus:
        parsed_input = json.loads(input)
        return self.from_dict(parsed_input)


class BlockchainStatusJSONParser:
    def __init__(self) -> None:
        self.__token_status_parser = TokenStatusJSONParser()

    def __parse_token_info(self, token_info: Dict[str, Any]) -> TokenStatus:
        return self.__token_status_parser.from_dict(token_info)

    def __get_token_status_list(self, tokens: List[Dict]) -> List[TokenStatus]:
        return [*map(lambda t: self.__parse_token_info(t), tokens)]

    def from_dict(self, parsed_input: Dict[str, Any]):
        return BlockchainStatus(
            chain_id=parsed_input.get("chain_id"),
            block_height=parsed_input.get("block_height"),
            block_time=parsed_input.get("block_time"),
            total_txs_num=parsed_input.get("total_txs_num"),
            total_validator_num=parsed_input.get("total_validator_num"),
            unjailed_validator_num=parsed_input.get("unjailed_validator_num"),
            jailed_validator_num=parsed_input.get("jailed_validator_num"),
            total_supply_tokens=self.__get_token_status_list(parsed_input.get("total_supply_tokens").get("supply")),
            total_circulating_tokens=self.__get_token_status_list(
                parsed_input.get("total_circulating_tokens").get("supply")
            ),
            bonded_tokens=parsed_input.get("bonded_tokens"),
            not_bonded_tokens=parsed_input.get("not_bonded_tokens"),
            inflation=parsed_input.get("inflation"),
            community_pool=self.__get_token_status_list(parsed_input.get("community_pool")),
            timestamp=parsed_input.get("timestamp"),
        )

    def parse(self, input: str) -> BlockchainStatus:
        parsed_input = json.loads(input)
        return self.from_dict(parsed_input)
