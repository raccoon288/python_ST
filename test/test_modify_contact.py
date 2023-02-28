from model.contact import Contact


def test_modify_first_contact_name(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first_contact_name(Contact(firstname="Iv", middlename="Iv", lastname="Iv",
                                                  nickname="van"))
    app.session.logout()


def test_modify_first_contact_photo(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first_contact_photo(Contact(image_name="test_image2.jpg"))
    app.session.logout()


def test_modify_first_contact_company(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first_contact_company(Contact(title="lalala", company="lalala",
                                                     address="Street"))
    app.session.logout()


def test_modify_first_contact_tel(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first_contact_tel(Contact(home_number="111", mobile_number="111",
                                                 work_number="111", fax="123"))
    app.session.logout()


def test_modify_first_contact_email(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first_contact_email(Contact(email="example11@mail.ru", email2="example22@mail.ru",
                                                   email3="example33@mail.ru", homepage="gooooooogle.com"))
    app.session.logout()


def test_modify_first_contact_date(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first_contact_date(Contact(bday="15", bmonth="October", byear="1996",
                                                  aday="25", amonth="October", ayear="2011"))
    app.session.logout()


def test_modify_first_contact_secondary(app):
    app.session.login(login="admin", password="secret")
    app.contact.modify_first_contact_secondary(Contact(address2="Street", phone2="phone", notes="lalalalalalal"))
    app.session.logout()
