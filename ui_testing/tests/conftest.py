import pytest

from ui_testing.helpers.session import create_session


@pytest.fixture(scope="session")
def session():
    session = create_session()
    yield session
    session.close()
