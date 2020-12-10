import pytest
import time

def check_batteria_funzionante():
    print("controllo batteria")
    assert False

@pytest.mark.skipif(check_batteria_funzionante == True, reason="Test accensione motore annullato se batteria non utilizzabile")
def test_automobile_si_puo_accendere():
    print("tento di accendere il veicolo")
    assert True

@pytest.mark.skip("in sviluppo")
def test_automobile_si_puo_spegnere():
    assert False

@pytest.mark.slow
def test_automobile_sensore_luminosita_interna():
    assert True


@pytest.mark.parametrize('posizione',['davanti_destra','davanti_sinistra','dietro_destra','dietro_sinistra'])
def test_freccia(posizione):
    print("sto testando la lampadina in posizione " + posizione)


def test_utente_login(get_db_connection):
    db = get_db_connection
    assert "connessione"=="connessione"

def test_delete_utente(get_db_connection):
    db = get_db_connection
    assert "cancellazione"=="cancellazione"

@pytest.mark.parametrize(
    'get_db_connection',
    [
        '192.168.1.1',
        '192.168.1.2'
    ],
    indirect=True
)
def test_delete_utente_parametrizzato(get_db_connection):
    assert True==True

def test_con_Skipif():
    utenti = []
    if len(utenti) == 0:
        pytest.skip("non puoi eseguire questo test se non hai questa condizione")

def test_con_fail():
    utenti = []
    if len(utenti) == 0:
        pytest.fail("questa condizione non doveva poter avvenire, qualcosa non funziona!")