from datetime import datetime, timezone
from typing import List

import pytest

from cosmos_client_rest.tokens import Token, TokenPrice
from cosmos_client_rest.tokens.parsers import *

sample_string_1 = """[
    {
        "denom": "uatom",
        "prices": [
            {
                "currency": "usd",
                "current_price": 31.61,
                "total_volume": 2141915525.8503935,
                "daily_price_change_in_percentage": -9.751876631636865,
                "market_cap": 9062540262.26136
            }
        ],
        "last_updated": "2022-01-27T09:47:29Z"
    }
]"""

expected_output_1 = [
    Token(
        "uatom",
        [TokenPrice("usd", 31.61, 2141915525.8503935, -9.751876631636865, 9062540262.26136)],
        datetime(2022, 1, 27, 9, 47, 29, tzinfo=timezone.utc),
    )
]


sample_string_2 = """[
    {
        "denom": "uatom",
        "prices": [
            {
                "currency": "usd",
                "current_price": 31.61,
                "total_volume": 2141915525.8503935,
                "daily_price_change_in_percentage": -9.751876631636865,
                "market_cap": 9062540262.26136
            }
        ],
        "last_updated": "2022-01-27T09:47:29Z"
    },
    {
        "denom": "bitcoin",
        "prices": [
            {
                "currency": "ron",
                "current_price": 0.611,
                "total_volume": 2141915525.8503935,
                "daily_price_change_in_percentage": -9.751876631636865,
                "market_cap": 9062540262.26136
            },
            {
                "currency": "usd",
                "current_price": 999.9,
                "total_volume": 2141915525.8503935,
                "daily_price_change_in_percentage": -9.751876631636865,
                "market_cap": 9062540262.26136
            }
        ],
        "last_updated": "2023-01-27T09:47:29Z"
    }
]"""

expected_output_2 = [
    Token(
        "uatom",
        [TokenPrice("usd", 31.61, 2141915525.8503935, -9.751876631636865, 9062540262.26136)],
        datetime(2022, 1, 27, 9, 47, 29, tzinfo=timezone.utc),
    ),
    Token(
        "bitcoin",
        [
            TokenPrice("ron", 0.611, 2141915525.8503935, -9.751876631636865, 9062540262.26136),
            TokenPrice("usd", 999.9, 2141915525.8503935, -9.751876631636865, 9062540262.26136),
        ],
        datetime(2023, 1, 27, 9, 47, 29, tzinfo=timezone.utc),
    ),
]


@pytest.mark.parametrize(
    ("sample_token_list", "expected_result"),
    [
        (sample_string_1, expected_output_1),
        (sample_string_2, expected_output_2),
    ],
)
def test_parser(sample_token_list, expected_result):
    parser = TokenJSONParser()
    result = parser.parse(sample_token_list)
    assert isinstance(result, List)
    assert result == expected_result
