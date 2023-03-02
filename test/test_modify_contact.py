from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.contact.modify_first(Contact(firstname="Ho"))


def test_modify_first_contact_middlename(app):
    app.contact.modify_first(Contact(middlename="Hoho"))


def test_modify_first_contact_lastname(app):
    app.contact.modify_first(Contact(lastname="Hohoho"))


def test_modify_first_contact_nickname(app):
    app.contact.modify_first(Contact(nickname="Hohohoho"))


def test_modify_first_contact_photo(app):
    app.contact.modify_first(Contact(image_name="test_image2.jpg"))


def test_modify_first_contact_title(app):
    app.contact.modify_first(Contact(title="lalala"))


def test_modify_first_contact_company(app):
    app.contact.modify_first(Contact(company="lalala"))


def test_modify_first_contact_address(app):
    app.contact.modify_first(Contact(address="Street"))


def test_modify_first_contact_home_number(app):
    app.contact.modify_first(Contact(home_number="111"))


def test_modify_first_contact_mobile_number(app):
    app.contact.modify_first(Contact(mobile_number="111"))


def test_modify_first_contact_work_number(app):
    app.contact.modify_first(Contact(work_number="111"))


def test_modify_first_contact_fax(app):
    app.contact.modify_first(Contact(fax="123"))


def test_modify_first_contact_email(app):
    app.contact.modify_first(Contact(email="example11@mail.ru"))


def test_modify_first_contact_email2(app):
    app.contact.modify_first(Contact(email2="example22@mail.ru"))


def test_modify_first_contact_email3(app):
    app.contact.modify_first(Contact(email3="example33@mail.ru"))


def test_modify_first_contact_homepage(app):
    app.contact.modify_first(Contact(homepage="gooooooogle.com"))


def test_modify_first_contact_bday(app):
    app.contact.modify_first(Contact(bday="15"))


def test_modify_first_contact_bmonth(app):
    app.contact.modify_first(Contact(bmonth="October"))


def test_modify_first_contact_byear(app):
    app.contact.modify_first(Contact(byear="1996"))


def test_modify_first_contact_aday(app):
    app.contact.modify_first(Contact(aday="25"))


def test_modify_first_contact_amonth(app):
    app.contact.modify_first(Contact(amonth="October"))


def test_modify_first_contact_ayear(app):
    app.contact.modify_first(Contact(ayear="2011"))


def test_modify_first_contact_address2(app):
    app.contact.modify_first(Contact(address2="Street"))


def test_modify_first_contact_phone2(app):
    app.contact.modify_first(Contact(phone2="phone"))


def test_modify_first_contact_notes(app):
    app.contact.modify_first(Contact(notes="lalalalalalal"))
