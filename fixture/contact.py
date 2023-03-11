import os
from model.contact import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                lastname = element.find_element_by_xpath("./td[2]").text
                firstname = element.find_element_by_xpath("./td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)

    def create(self, contact):
        wd = self.app.wd
        # open home page
        self.app.navigation.open_home_page()
        # init add contact
        wd.find_element_by_link_text("add new").click()
        # add contact
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_name("submit").click()
        self.app.navigation.return_to_home_page()
        # reset cash
        self.contact_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # open home page
        self.app.navigation.open_home_page()
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # delete contact
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.navigation.return_to_home_page()
        WebDriverWait(wd, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        # reset cash
        self.contact_cache = None

    def modify_first(self, contact):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        # open home page
        self.app.navigation.open_home_page()
        # select contact and edit
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # change field
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()
        # reset cash
        self.contact_cache = None
