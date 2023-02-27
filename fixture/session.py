import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        print(wd.find_element_by_name("logout"))
        wd.find_element_by_link_text("Logout").click()
        time.sleep(2)



