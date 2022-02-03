from unittest.mock import patch

import pytest


@pytest.fixture(scope="function")
def sample_blockchain_status():
    # TODO replace with os.path.join
    with open("tests/unit/blockchain/sample_status.json", "r") as f:
        return f.read()


@pytest.fixture(scope="function", autouse=True)
def mock_api(sample_blockchain_status):
    with patch("cosmos_client_rest.blockchain.api_get_blockchain_status") as mock:
        mock.return_value = sample_blockchain_status
        yield
