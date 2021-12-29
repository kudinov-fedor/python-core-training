import pytest


@pytest.fixture(scope="session")
def host() -> str:
    return "https://www.w3schools.com"
