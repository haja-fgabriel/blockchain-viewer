from datetime import datetime
from .factories import TokenFactory
from cosmos_client.tokens import Token


def test_token_factory():
    instance = TokenFactory.build()
    assert isinstance(instance, Token)
    assert instance.denom
    assert instance.prices is not None
    assert isinstance(instance.last_updated, datetime)
