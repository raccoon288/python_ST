from model.group import Group


def test_modify_first_group_name(app):
    app.group.modify_first(Group(name="Hohoho"))


def test_modify_first_group_header(app):
    app.group.modify_first(Group(header="Hohoho"))


def test_modify_first_group_footer(app):
    app.group.modify_first(Group(footer="Hohoho"))
