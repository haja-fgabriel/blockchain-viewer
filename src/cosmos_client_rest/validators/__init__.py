from cosmos_client_rest.validators.parsers.json import ValidatorJSONParser
from .api import get_validators as api_get_validators
from .models import *


def get_validators():
    parser = ValidatorJSONParser()
    return parser.parse(api_get_validators())
