import pytest
from fixture.application import Appication

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Appication()
    else:
        if not fixture.is_valid():
            fixture = Appication()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
