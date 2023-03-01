from model.group import Group


def test_modify_first_group_name(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first(Group(name="Hohoho"))
    app.session.logout()


def test_modify_first_group_header(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first(Group(header="Hohoho"))
    app.session.logout()


def test_modify_first_group_footer(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first(Group(footer="Hohoho"))
    app.session.logout()
