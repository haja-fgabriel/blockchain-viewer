from unittest.mock import patch

import pytest


@pytest.fixture
def sample_validator_list():
    with open("tests/unit/validators/sample_validators.json", "r") as f:
        return f.read()


@pytest.fixture(scope="function", autouse=True)
def mock_api(sample_validator_list):
    with patch("cosmos_client.validators.api_get_validators") as mock:
        mock.return_value = sample_validator_list
        yield mock
