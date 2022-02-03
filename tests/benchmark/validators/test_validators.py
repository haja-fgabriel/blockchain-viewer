from typing import List

from cosmos_client.validators import get_validators, Validator, ValidatorUptime


def test_get_validators():
    result = get_validators()
    assert isinstance(result, List)
    for validator in result:
        assert isinstance(validator, Validator)
