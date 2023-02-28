# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group(name="example1", header="example1", footer="example1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
