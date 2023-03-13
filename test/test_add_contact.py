# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


testdata = [
            Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                      nickname="vanek", image_name="test_image.jpg", title="example",
                      company="berc", address="Saint Petersburg, Nevskiy Avenue",
                      home_number="12345678", mobile_number="1234567", work_number="123456789",
                      fax="123", email="exampleq@mail.ru", email2="example2@mail.ru",
                      email3="example3@mail.ru", homepage="google.com", bday="20",
                      bmonth="November", byear="1996", aday="30", amonth="December",
                      ayear="2000", address2="Saint Petersburg, Sadovaya Street",
                      phone2="12365485", notes="la"),
            Contact(firstname="", middlename="", lastname="",
                      nickname="", image_name=None, title="",
                      company="", address="",
                      home_number="", mobile_number="", work_number="",
                      fax="", email="", email2="",
                      email3="", homepage="", bday="",
                      bmonth="", byear="", aday="", amonth="",
                      ayear="", address2="",
                      phone2="", notes="")
]


@pytest.mark.parametrize("contact", testdata, ids=(repr(x) for x in testdata))
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
    #                   nickname="vanek", image_name="test_image.jpg", title="example",
    #                   company="berc", address="Saint Petersburg, Nevskiy Avenue",
    #                   home_number="12345678", mobile_number="1234567", work_number="123456789",
    #                   fax="123", email="exampleq@mail.ru", email2="example2@mail.ru",
    #                   email3="example3@mail.ru", homepage="google.com", bday="20",
    #                   bmonth="November", byear="1996", aday="30", amonth="December",
    #                   ayear="2000", address2="Saint Petersburg, Sadovaya Street",
    #                   phone2="12365485", notes="la")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middlename="", lastname="",
#                       nickname="", image_name=None, title="",
#                       company="", address="",
#                       home_number="", mobile_number="", work_number="",
#                       fax="", email="", email2="",
#                       email3="", homepage="", bday="",
#                       bmonth="", byear="", aday="", amonth="",
#                       ayear="", address2="",
#                       phone2="", notes="")
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



