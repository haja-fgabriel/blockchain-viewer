import pytest

# import ipdb

# ipdb.set_trace()
from blockchain_viewer.app import app


@pytest.fixture
def rest_client():
    app.testing = True
    app.debug = True
    yield app.test_client()


def test_client(rest_client):

    pass
