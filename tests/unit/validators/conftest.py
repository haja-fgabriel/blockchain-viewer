from unittest.mock import patch, Mock

import pytest


@pytest.fixture
def sample_validator_list():
    with open("tests/unit/validators/sample_validators.json", "r") as f:
        return f.read()


@pytest.fixture
def sample_block_list():
    with open("tests/unit/validators/sample_block_list.json", "r") as f:
        return f.read()


@pytest.fixture(scope="function", autouse=True)
def mock_api(monkeypatch, sample_validator_list, sample_block_list):
    monkeypatch.setattr("cosmos_client.validators.api_get_validators", Mock(return_value=sample_validator_list))
    monkeypatch.setattr("cosmos_client.validators.api_get_validator_blocks", Mock(return_value=sample_block_list))
    yield
