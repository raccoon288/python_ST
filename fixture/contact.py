import os
from model.contact import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re


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
                head_path = os.path.split(os.getcwd())[0]
                path = os.path.join(head_path, "addressbook tests\image", text)
                wd.find_element_by_name(field_name).send_keys(path)
            elif field_name == "bday" or field_name == "bmonth" or field_name == "aday" or field_name == "amonth":
                wd.find_element_by_name(field_name).send_keys(text)
            else:
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def clear_symbols_in_phones(self, phone):
        return re.sub("[() -]", "", phone)

    def merge_all_phones(self, contact):
        phones_without_none = filter(lambda x: x is not None,
                                     [contact.home_number,
                                      contact.mobile_number,
                                      contact.work_number,
                                      contact.phone2])
        phones_without_other_symbols = map(lambda x: self.clear_symbols_in_phones(x), phones_without_none)
        phones_without_empty_lines = filter(lambda x: x != "", phones_without_other_symbols)
        return "\n".join(phones_without_empty_lines)

    def merge_all_emails(self, contact):
        emails_without_none = filter(lambda x: x is not None,
                                     [contact.email,
                                      contact.email2,
                                      contact.email3])
        emails_without_empty_lines = filter(lambda x: x != "", emails_without_none)
        return "\n".join(emails_without_empty_lines)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

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
                all_phones = element.find_element_by_xpath("./td[6]").text
                all_emails = element.find_element_by_xpath("./td[5]").text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home_number=home_number, mobile_number=mobile_number,
                       work_number=work_number, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_number=home_number, mobile_number=mobile_number,
                       work_number=work_number, phone2=phone2)

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
        self.select_contact_by_index(index)
        # delete contact
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.app.navigation.return_to_home_page()
        # reset cash
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # open home page
        self.app.navigation.open_home_page()
        self.select_contact_by_id(id)
        # delete contact
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.app.navigation.return_to_home_page()
        # reset cash
        self.contact_cache = None

    def modify_first(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        # open home page
        self.app.navigation.open_home_page()
        self.open_contact_to_edit_by_index(index)
        # change field
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()
        # reset cash
        self.contact_cache = None

    def modify_contact_by_id(self, contact):
        wd = self.app.wd
        # open home page
        self.app.navigation.open_home_page()
        self.open_contact_to_edit_by_id(contact.id)
        # change field
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()
        # reset cash
        self.contact_cache = None

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        # open home page
        self.app.navigation.open_home_page()
        # select contact
        self.select_contact_by_id(contact.id)
        # select group
        self.app.group.select_group_to_add_by_id_on_homepage(group.id)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Add to']").click()
        # return to homepage
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def delete_contact_from_group(self, contact, group):
        wd = self.app.wd
        # open home page
        self.app.navigation.open_home_page()
        # select group
        self.app.group.select_group_to_delete_by_id_on_homepage(group.id)
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % contact.id).click()
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@name='remove']").click()
        # return to homepage
        self.app.navigation.return_to_home_page()
        self.contact_cache = None





