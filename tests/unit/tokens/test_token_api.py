from typing import List

from cosmos_client.tokens import get_tokens, Token


def test_get_tokens():
    result = get_tokens("uatom")
    assert isinstance(result, List)
    for token in result:
        assert isinstance(token, Token)
