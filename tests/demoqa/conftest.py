import pytest


@pytest.fixture(scope="session")
def host() -> str:
    return "https://demoqa.com"
