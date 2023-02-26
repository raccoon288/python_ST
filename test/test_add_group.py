# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(login="admin", password="secret")
    app.create_group(Group(name="example", header="example", footer="example"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(login="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
