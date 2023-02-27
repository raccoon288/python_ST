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
