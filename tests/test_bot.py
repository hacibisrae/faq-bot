"""Tests automatiques du bot et de l'application (lancés avec : pytest)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402
from bot import REPONSE_PAR_DEFAUT, repondre  # noqa: E402


def test_salutation():
    assert "Bonjour" in repondre("Salut !")


def test_majuscules_et_accents():
    assert "branche" in repondre("C'est quoi une BRANCHE ?").lower()


def test_question_inconnue():
    assert repondre("Quelle est la météo ?") == REPONSE_PAR_DEFAUT


def test_merci_ne_declenche_pas_ci():
    assert repondre("merci") == "Avec plaisir ! 😊"


def test_route_chat():
    client = app.test_client()
    reponse = client.post("/chat", json={"message": "docker"})
    assert reponse.status_code == 200
    assert "conteneur" in reponse.get_json()["reponse"]


def test_route_health():
    client = app.test_client()
    assert client.get("/health").get_json() == {"status": "ok"}
