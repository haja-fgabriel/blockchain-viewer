import re
from typing import Dict, List
from unittest.mock import Mock
from cosmos_client import blockchain

from cosmos_client.blockchain import get_block_status, get_blockchain_status, BlockchainStatus


def test_get_blockchain_status():
    result = get_blockchain_status()
    assert isinstance(result, BlockchainStatus)
    assert result.chain_id == "cosmoshub-4"
    assert result.block_height == 9288744


def assert_is_block_valid(block):
    assert isinstance(block, Dict)
    assert isinstance(block.get("id"), str)
    assert block.get("chainid") == "cosmoshub-4"
    assert isinstance(block.get("height"), str)
    assert re.match(r"[0-9a-fA-F]+", block.get("proposer"))
    assert re.match(r"[0-9a-fA-F]+", block.get("block_hash"))
    assert isinstance(block.get("num_signatures"), str)
    assert isinstance(block.get("num_txs"), str)
    assert isinstance(block.get("block_round"), int)
    assert block.get("block_round") >= 0
    assert isinstance(block.get("gas_wanted"), int)
    assert block.get("gas_wanted") >= 0
    assert isinstance(block.get("gas_used"), int)
    assert block.get("gas_used") >= 0
    assert isinstance(block.get("txs"), List)
    assert isinstance(block.get("timestamp"), str)


def assert_is_transaction_valid(tx):
    assert isinstance(tx, Dict)
    assert isinstance(tx.get("header"), Dict)
    assert set(tx.get("header").keys()) == {"id", "chain_id", "block_id", "timestamp"}
    tx_data = tx.get("data")
    assert isinstance(tx_data, Dict)
    assert isinstance(tx_data.get("height"), str)
    assert isinstance(tx_data.get("timestamp"), str)
    assert re.match(r"[0-9a-fA-F]+", tx_data.get("txhash"))
    assert re.match(r"[0-9a-fA-F]+", tx_data.get("data"))
    assert isinstance(tx_data.get("logs"), List)
    for log in tx_data.get("logs"):
        assert_transaction_log_valid(log)
    assert isinstance(tx_data.get("gas_wanted"), str)
    assert isinstance(tx_data.get("gas_used"), str)
    tx_description = tx_data.get("tx")
    assert isinstance(tx_description, Dict)
    assert isinstance(tx_description.get("@type"), str)
    tx_description_body = tx_description.get("body")
    assert isinstance(tx_description_body, Dict)
    assert isinstance(tx_description_body.get("messages"), List)
    for msg in tx_description_body.get("messages"):
        assert_transaction_message_valid(msg)
    tx_auth_info = tx_description.get("auth_info")
    assert isinstance(tx_auth_info, Dict)
    tx_fee = tx_auth_info.get("fee")
    assert isinstance(tx_fee, Dict)
    assert isinstance(tx_fee.get("amount"), List)
    for amount in tx_fee.get("amount"):
        assert {"denom", "amount"} == set(amount.keys())


def assert_transaction_message_valid(msg):
    assert {"@type", "from_address", "to_address", "amount"} == set(msg.keys())
    assert isinstance(msg.get("amount"), List)
    for amount in msg.get("amount"):
        assert {"denom", "amount"} == set(amount.keys())


def assert_transaction_log_valid(log):
    assert isinstance(log.get("msg_index"), int) and log.get("msg_index") >= 0
    assert isinstance(log.get("events"), List)
    for event in log.get("events"):
        assert isinstance(event, Dict)
        assert set(event.keys()) == {"type", "attributes"}
        assert all({"key", "value"} == set(attr.keys()) for attr in event.get("attributes"))


def test_get_block_status():
    result = get_block_status("cosmoshub-4", 9309064)
    assert isinstance(result, List)
    for block in result:
        assert_is_block_valid(block)
        for tx in block.get("txs"):
            assert_is_transaction_valid(tx)
