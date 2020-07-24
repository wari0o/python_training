import pytest
from fixture.application import Appication


@pytest.fixture(scope="session")
def app(request):
    fixture = Appication()
    request.addfinalizer(fixture.destroy)
    return fixture
