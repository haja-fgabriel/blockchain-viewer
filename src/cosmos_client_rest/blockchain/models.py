from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class TokenStatus:
    denom: str
    amount: str


@dataclass
class BlockchainStatus:
    chain_id: str
    block_height: int
    block_time: float
    total_txs_num: int  # Total number of transactions
    total_validator_num: int
    unjailed_validator_num: int
    jailed_validator_num: int
    total_supply_tokens: List[TokenStatus]
    total_circulating_tokens: List[TokenStatus]
    bonded_tokens: int
    not_bonded_tokens: int
    inflation: str
    community_pool: List[TokenStatus]
    timestamp: datetime
