from unittest.mock import patch, Mock

import pytest


@pytest.fixture(scope="function")
def mock_get_tokens_api():
    with patch("cosmos_client_rest.tokens.api.get") as mock:
        # mock.return_value =
        yield mock
