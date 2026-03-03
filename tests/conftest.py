from pytest import fixture
from lib.database_connection import DatabaseConnection
import pytest
from main import app

@fixture
def db_conn():
    conn = DatabaseConnection()
    conn.connect()
    return conn


@pytest.fixture
def web_client():
    with app.test_client() as client:
        yield client
