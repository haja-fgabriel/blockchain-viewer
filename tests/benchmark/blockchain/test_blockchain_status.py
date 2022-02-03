from cosmos_client.blockchain import get_blockchain_status, BlockchainStatus


def test_get_blockchain_status():
    result = get_blockchain_status()
    assert isinstance(result, BlockchainStatus)
    assert result.chain_id == "cosmoshub-4"
    assert result.block_height > 9288744
