from unittest.mock import Mock

from cosmos_client_rest.blockchain import get_blockchain_status, BlockchainStatus


def test_get_blockchain_status():
    result = get_blockchain_status()
    assert isinstance(result, BlockchainStatus)
    pass
