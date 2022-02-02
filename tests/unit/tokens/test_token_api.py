from typing import List

from cosmos_client_rest.tokens import get_tokens, Token


def test_get_tokens():
    result = get_tokens()
    assert isinstance(result, List)
    for token in result:
        assert isinstance(token, Token)
