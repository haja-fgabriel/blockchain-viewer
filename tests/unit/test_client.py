from dataclasses import fields
from datetime import datetime
from unittest.mock import Mock, patch

from cosmos_client_rest.tokens import TokenPrice, Token

import pytest


def get_dataclass_field_names(cls):
    return [*map(lambda f: f.name, fields(cls))]


@pytest.fixture
def mock_price():
    mock = Mock(spec=get_dataclass_field_names(TokenPrice))
    mock.currency = "ron"
    mock.current_price = 0.1
    mock.total_volume = 1000000000.0
    mock.daily_price_change_in_percentage = -1.2
    mock.market_cap = 1001010101.0
    return mock


@pytest.fixture
def mock_token(mock_price):
    mock = Mock(spec=get_dataclass_field_names(Token))
    mock.denom = "uatom"
    mock.prices = [mock_price]
    mock.last_updated = datetime(2022, 1, 27, 9, 47, 29)
    return mock


def get_tokens():
    return []


@pytest.fixture
def mock_get_tokens(mock_token):
    with patch("test_client.get_tokens") as mock:
        mock.return_value = [mock_token]
        yield mock


def test_get_tokens(mock_get_tokens):
    assert isinstance(get_tokens, Mock)
    result = get_tokens()
    assert len(result) == 1
    token = result[0]
    assert isinstance(token, Mock)
    assert token.denom == "uatom"
    assert len(token.prices) == 1
    price = token.prices[0]
    assert isinstance(price, Mock)
    assert price.currency == "ron"
    assert price.total_volume == 1000000000.0
    assert price.current_price == 0.1


def test_mock_price(mock_price):
    assert isinstance(mock_price, Mock)
    assert mock_price.currency == "ron"
    assert mock_price.current_price == 0.1
