def test_delete_first_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()
