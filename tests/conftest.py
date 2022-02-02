from unittest.mock import patch, Mock

import pytest


@pytest.fixture(scope="function", autouse=True)
def mock_get_tokens_api():
    with patch("cosmos_client_rest.blockchain.api_get_blockchain_status") as mock:
        yield mock
