import os


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init add contact
        wd.find_element_by_link_text("add new").click()
        # add contact
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # if contact.image_name != "":
        #     wd.find_element_by_name("photo").send_keys(os.path.join(os.path.dirname(os.getcwd()), "image",
        #                                                             contact.image_name))
        if contact.image_name != "":
            wd.find_element_by_name("photo").send_keys(os.path.join('C:\Learning\Python_ST_2\python_ST\image',
                                                                    contact.image_name))
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home_number)
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)
        wd.find_element_by_name("work").send_keys(contact.work_number)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").send_keys(contact.bday)
        wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").send_keys(contact.aday)
        wd.find_element_by_name("amonth").send_keys(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
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

    def modify_first_contact_name(self, contact):
        wd = self.app.wd
        # select contact and edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # change firstname, middlename, lastname, nickname
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()

    def modify_first_contact_photo(self, contact):
        wd = self.app.wd
        # select contact and edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # change photo
        wd.find_element_by_name("photo").send_keys(os.path.join('C:\Learning\Python_ST_2\python_ST\image',
                                                                contact.image_name))
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()

    def modify_first_contact_company(self, contact):
        wd = self.app.wd
        # select contact and edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # change title, company, address
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()

    def modify_first_contact_tel(self, contact):
        wd = self.app.wd
        # select contact and edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # change home, mobile, work, fax
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_number)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_number)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()

    def modify_first_contact_email(self, contact):
        wd = self.app.wd
        # select contact and edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # change email, email2, email3, homepage
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()

    def modify_first_contact_date(self, contact):
        wd = self.app.wd
        # select contact and edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # change bday, bmonth, byear, aday, amonth, ayear
        wd.find_element_by_name("bday").send_keys(contact.bday)
        wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").send_keys(contact.aday)
        wd.find_element_by_name("amonth").send_keys(contact.amonth)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()

    def modify_first_contact_secondary(self, contact):
        wd = self.app.wd
        # select contact and edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # change address2, phone2, notes
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit
        wd.find_element_by_xpath("//input[@type='submit'][@value='Update']").click()
        self.app.navigation.return_to_home_page()
