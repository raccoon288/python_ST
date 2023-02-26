# -*- coding: utf-8 -*-

import unittest
from contact import Contact
from Application import Application


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(login="admin", password="secret")
        self.app.add_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                                     nickname="vanek", image_name="test_image.jpg", title="example",
                                     company="berc", address="Saint Petersburg, Nevskiy Avenue",
                                     home_number="12345678", mobile_number="1234567", work_number="123456789",
                                     fax="123", email="exampleq@mail.ru", email2="example2@mail.ru",
                                     email3="example3@mail.ru", homepage="google.com", bday="16",
                                     bmonth="November", byear="1996", aday="18", amonth="December",
                                     ayear="2000", address2="Saint Petersburg, Sadovaya Street",
                                     phone2="Saint Petersburg", notes="lalalala"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
