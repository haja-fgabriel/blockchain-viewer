from dataclasses import dataclass


@dataclass
class ValidatorUptime:
    address: str
    missed_blocks: int
    over_blocks: int


@dataclass
class Validator:
    rank: int
    account_address: str
    operator_address: str
    consensus_pubkey: str
    jailed: bool
    status: int
    tokens: str
    delegator_shares: str
    moniker: str
    identity: str
    website: str
    details: str
    unbonding_height: str
    unbonding_time: str
    rate: str
    max_rate: str
    max_change_rate: str
    update_time: str
    uptime: ValidatorUptime
    min_self_delegation: str
    keybase_url: str
