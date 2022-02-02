__all__ = [
    "TokenPrice",
    "Token",
    "get_tokens",
]

from .api import get_tokens as api_get_tokens
from .models import *

from .parsers import TokenJSONParser


def get_tokens(token_id):
    parser = TokenJSONParser()
    return parser.parse(api_get_tokens(token_id))
