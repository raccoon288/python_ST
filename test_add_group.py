# -*- coding: utf-8 -*-
import unittest

from group import Group
from Application import Application


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(login="admin", password="secret")
        self.app.create_group(Group(name="example", header="example", footer="example"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(login="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
