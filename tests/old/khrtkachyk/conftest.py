import pytest
from khr_hw9_Frenchdeck import FrenchDeck


@pytest.fixture
def deck():
    return FrenchDeck()
