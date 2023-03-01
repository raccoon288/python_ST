from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(firstname="Ho"))
    app.session.logout()


def test_modify_first_contact_middlename(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(middlename="Hoho"))
    app.session.logout()


def test_modify_first_contact_lastname(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(lastname="Hohoho"))
    app.session.logout()


def test_modify_first_contact_nickname(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(nickname="Hohohoho"))
    app.session.logout()


def test_modify_first_contact_photo(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(image_name="test_image2.jpg"))
    app.session.logout()


def test_modify_first_contact_title(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(title="lalala"))
    app.session.logout()


def test_modify_first_contact_company(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(company="lalala"))
    app.session.logout()


def test_modify_first_contact_address(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(address="Street"))
    app.session.logout()


def test_modify_first_contact_home_number(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(home_number="111"))
    app.session.logout()


def test_modify_first_contact_mobile_number(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(mobile_number="111"))
    app.session.logout()


def test_modify_first_contact_work_number(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(work_number="111"))
    app.session.logout()


def test_modify_first_contact_fax(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(fax="123"))
    app.session.logout()


def test_modify_first_contact_email(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(email="example11@mail.ru"))
    app.session.logout()


def test_modify_first_contact_email2(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(email2="example22@mail.ru"))
    app.session.logout()


def test_modify_first_contact_email3(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(email3="example33@mail.ru"))
    app.session.logout()


def test_modify_first_contact_homepage(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(homepage="gooooooogle.com"))
    app.session.logout()


def test_modify_first_contact_bday(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(bday="15"))
    app.session.logout()


def test_modify_first_contact_bmonth(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(bmonth="October"))
    app.session.logout()


def test_modify_first_contact_byear(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(byear="1996"))
    app.session.logout()


def test_modify_first_contact_aday(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(aday="25"))
    app.session.logout()


def test_modify_first_contact_amonth(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(amonth="October"))
    app.session.logout()


def test_modify_first_contact_ayear(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(ayear="2011"))
    app.session.logout()


def test_modify_first_contact_address2(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(address2="Street"))
    app.session.logout()


def test_modify_first_contact_phone2(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(phone2="phone"))
    app.session.logout()


def test_modify_first_contact_notes(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first(Contact(notes="lalalalalalal"))
    app.session.logout()
