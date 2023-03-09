from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ho")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(middlename="Hoho"))


def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="Hohoho")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(nickname="Hohohoho"))


def test_modify_first_contact_photo(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(image_name="test_image2.jpg"))


def test_modify_first_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(title="lalala"))


def test_modify_first_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(company="lalala"))


def test_modify_first_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(address="Street"))


def test_modify_first_contact_home_number(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(home_number="111"))


def test_modify_first_contact_mobile_number(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(mobile_number="111"))


def test_modify_first_contact_work_number(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(work_number="111"))


def test_modify_first_contact_fax(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(fax="123"))


def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(email="example11@mail.ru"))


def test_modify_first_contact_email2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(email2="example22@mail.ru"))


def test_modify_first_contact_email3(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(email3="example33@mail.ru"))


def test_modify_first_contact_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(homepage="gooooooogle.com"))


def test_modify_first_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(bday="15"))


def test_modify_first_contact_bmonth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(bmonth="October"))


def test_modify_first_contact_byear(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(byear="1996"))


def test_modify_first_contact_aday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(aday="25"))


def test_modify_first_contact_amonth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(amonth="October"))


def test_modify_first_contact_ayear(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(ayear="2011"))


def test_modify_first_contact_address2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(address2="Street"))


def test_modify_first_contact_phone2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(phone2="phone"))


def test_modify_first_contact_notes(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.modify_first(Contact(notes="lalalalalalal"))
