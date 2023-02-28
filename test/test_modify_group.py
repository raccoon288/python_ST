from model.group import Group


def test_modify_first_group_name(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first_group_name(Group(name="la"))
    app.session.logout()


def test_modify_first_group_header(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first_group_header(Group(header="lalala"))
    app.session.logout()


def test_modify_first_group_footer(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first_group_footer(Group(footer="lalala"))
    app.session.logout()