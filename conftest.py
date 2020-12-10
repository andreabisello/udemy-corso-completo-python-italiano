import pytest
import time
from pytest_testconfig import config



@pytest.fixture(scope="module")
def get_db_connection(request):
    time.sleep(3)
    db = "..."
    url_connessione = config['database']['url']
    username_connessione = config['utenti']['username']
    print(url_connessione)
    print(username_connessione)
    return db
