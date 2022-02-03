from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class TokenPrice:
    currency: str
    current_price: float
    total_volume: float
    daily_price_change_in_percentage: float
    market_cap: float


@dataclass
class Token:
    denom: str
    prices: List[TokenPrice]
    last_updated: datetime
