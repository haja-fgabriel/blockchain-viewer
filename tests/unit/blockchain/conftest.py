from unittest.mock import patch, Mock

import pytest


@pytest.fixture(scope="function")
def sample_hub_status():
    # TODO replace with os.path.join
    with open("tests/unit/blockchain/sample_status.json", "r") as f:
        return f.read()


@pytest.fixture(scope="function")
def sample_block_status():
    with open("tests/unit/blockchain/sample_block.json", "r") as f:
        return f.read()


@pytest.fixture(scope="function", autouse=True)
def mock_api(monkeypatch, sample_hub_status, sample_block_status):
    monkeypatch.setattr("cosmos_client.blockchain.api_get_blockchain_status", Mock(return_value=sample_hub_status))
    monkeypatch.setattr("cosmos_client.blockchain.api_get_block_status", Mock(return_value=sample_block_status))
    yield
