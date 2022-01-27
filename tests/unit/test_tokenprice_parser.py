import pytest

from cosmos_client_rest.tokens import TokenPrice
from cosmos_client_rest.tokens.parsers import TokenPriceJSONParser

input_string_1 = """[
    {
        "currency": "usd",
        "current_price": 31.61,
        "total_volume": 2141915525.8503935,
        "daily_price_change_in_percentage": -9.751876631636865,
        "market_cap": 9062540262.26136
    }
]"""

expected_output_1 = [
    TokenPrice("usd", 31.61, 2141915525.8503935, -9.751876631636865, 9062540262.26136),
]

input_string_2 = """[
    {
        "currency": "usd",
        "current_price": 31.61,
        "total_volume": 2141915525.8503935,
        "daily_price_change_in_percentage": -9.751876631636865
        "market_cap": 9062540262.26136
    },
    {
        "currency": "ron",
        "current_price": 0.01,
        "total_volume": 21410915525.8503935,
        "daily_price_change_in_percentage": -99.751876631636865
        "market_cap": 9062540262.26136
    }
]"""

expected_output_2 = [
    TokenPrice("usd", 31.61, 2141915525.8503935, -9.751876631636865, 9062540262.26136),
    TokenPrice("ron", 0.01, 21410915525.8503935, -99.751876631636865, 9062540262.26136),
]


@pytest.mark.parametrize(
    ("input_string", "expected"),
    [
        (input_string_1, expected_output_1),
    ],
)
def test_tokenprice_parser(input_string, expected):
    parser = TokenPriceJSONParser()
    result = parser.parse(input_string)
    assert result == expected
    pass
