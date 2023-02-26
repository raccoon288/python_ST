# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.add_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                            nickname="vanek", image_name="test_image.jpg", title="example",
                            company="berc", address="Saint Petersburg, Nevskiy Avenue",
                            home_number="12345678", mobile_number="1234567", work_number="123456789",
                            fax="123", email="exampleq@mail.ru", email2="example2@mail.ru",
                            email3="example3@mail.ru", homepage="google.com", bday="16",
                            bmonth="November", byear="1996", aday="18", amonth="December",
                            ayear="2000", address2="Saint Petersburg, Sadovaya Street",
                            phone2="Saint Petersburg", notes="lalalala"))
    app.session.logout()


