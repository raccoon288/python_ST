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
        wd.find_element_by_link_text("Logout").click()
        time.sleep(2)

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, login):
        wd = self.app.wd
        return wd.find_element_by_xpath("/html/body/div/div[1]/form/b").text == "("+login+")"

    def ensure_login(self, login, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(login):
                return
            else:
                self.logout()
        self.login(login, password)

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()
