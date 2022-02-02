from datetime import datetime, timezone
from typing import List

import pytest

from cosmos_client_rest.tokens import Token, TokenPrice
from cosmos_client_rest.tokens.parsers import *


def test_parser(token_parser_args):
    token_string, expected_result = token_parser_args
    parser = TokenJSONParser()
    result = parser.parse(token_string)
    assert isinstance(result, List)
    assert result == expected_result
