import os


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        self.fill_field_value("firstname", contact.firstname)
        self.fill_field_value("middlename", contact.middlename)
        self.fill_field_value("lastname", contact.lastname)
        self.fill_field_value("nickname", contact.nickname)
        self.fill_field_value("photo", contact.image_name)
        self.fill_field_value("title", contact.title)
        self.fill_field_value("company", contact.company)
        self.fill_field_value("address", contact.address)
        self.fill_field_value("home", contact.home_number)
        self.fill_field_value("mobile", contact.mobile_number)
        self.fill_field_value("work", contact.work_number)
        self.fill_field_value("fax", contact.fax)
        self.fill_field_value("email", contact.email)
        self.fill_field_value("email2", contact.email2)
        self.fill_field_value("email3", contact.email3)
        self.fill_field_value("homepage", contact.homepage)
        self.fill_field_value("bday", contact.bday)
        self.fill_field_value("bmonth", contact.bmonth)
        self.fill_field_value("byear", contact.byear)
        self.fill_field_value("aday", contact.aday)
        self.fill_field_value("amonth", contact.amonth)
        self.fill_field_value("ayear", contact.ayear)
        self.fill_field_value("address2", contact.address2)
        self.fill_field_value("phone2", contact.phone2)
        self.fill_field_value("notes", contact.notes)

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name == "photo":
                wd.find_element_by_name(field_name).send_keys(os.path.join('C:\Learning\Python_ST_2\python_ST\image',
                                                                           text))
            elif field_name == "bday" or field_name == "bmonth" or field_name == "aday" or field_name == "amonth":
                wd.find_element_by_name(field_name).send_keys(text)
            else:
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init add contact
        wd.find_element_by_link_text("add new").click()
        # add contact
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_name("submit").click()
        self.app.navigation.return_to_home_page()

    def delete_first(self):
        wd = self.app.wd
        # select contact
        wd.find_element_by_name("selected[]").click()
        # delete contact
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.navigation.return_to_home_page()

    def modify_first(self, contact):
        wd = self.app.wd
        # select contact and edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # change field
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()
