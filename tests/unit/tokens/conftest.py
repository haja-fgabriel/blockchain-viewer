from datetime import datetime, timezone
from unittest.mock import patch

import pytest
from cosmos_client_rest.tokens import Token, TokenPrice
from cosmos_client_rest.tokens.parsers import *


token_inputstring_1 = """[
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

token_inputstring_2 = """[
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

sample_input_strings = [
    token_inputstring_1,
    token_inputstring_2,
]


expected_output_1 = [
    Token(
        "uatom",
        [TokenPrice("usd", 31.61, 2141915525.8503935, -9.751876631636865, 9062540262.26136)],
        datetime(2022, 1, 27, 9, 47, 29, tzinfo=timezone.utc),
    )
]

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

sample_expected_outputs = [
    expected_output_1,
    expected_output_2,
]


@pytest.fixture(scope="function", params=sample_input_strings)
def token_string(request):
    return request.param


@pytest.fixture(scope="function", params=sample_expected_outputs)
def parsed_token(request):
    return request.param


@pytest.fixture(scope="function", params=zip(sample_input_strings, sample_expected_outputs))
def token_parser_args(request):
    return request.param[0], request.param[1]


@pytest.fixture(scope="function", autouse=True)
def mock_api(monkeypatch, token_string):
    monkeypatch.setattr("cosmos_client_rest.tokens.api_get_tokens", lambda i: token_string)
    yield
