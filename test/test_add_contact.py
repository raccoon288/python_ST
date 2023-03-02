# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                               nickname="vanek", image_name="test_image.jpg", title="example",
                               company="berc", address="Saint Petersburg, Nevskiy Avenue",
                               home_number="12345678", mobile_number="1234567", work_number="123456789",
                               fax="123", email="exampleq@mail.ru", email2="example2@mail.ru",
                               email3="example3@mail.ru", homepage="google.com", bday="20",
                               bmonth="November", byear="1996", aday="30", amonth="December",
                               ayear="2000", address2="Saint Petersburg, Sadovaya Street",
                               phone2="Saint Petersburg", notes="la"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               nickname="", image_name=None, title="",
                               company="", address="",
                               home_number="", mobile_number="", work_number="",
                               fax="", email="", email2="",
                               email3="", homepage="", bday="",
                               bmonth="", byear="", aday="", amonth="",
                               ayear="", address2="",
                               phone2="", notes=""))


