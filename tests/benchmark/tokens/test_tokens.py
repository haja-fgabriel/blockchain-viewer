from typing import List
from cosmos_client.tokens import Token, get_tokens


def test_get_tokens():
    result = get_tokens("uatom")
    assert isinstance(result, List)
    assert len(result) > 0
    for token in result:
        assert isinstance(token, Token)
