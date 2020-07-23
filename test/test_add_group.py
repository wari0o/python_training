# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Appication

@pytest.fixture
def app(request):
    fixture = Appication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
