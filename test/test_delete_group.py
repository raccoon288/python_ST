def test_delete_first_group(app):
    app.session.login(login="admin", password="secret")
    app.group.delete_first()
    app.session.logout()
