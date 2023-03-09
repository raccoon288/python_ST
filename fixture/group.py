from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def fill_group_form(self, group):
        self.fill_field_value("group_name", group.name)
        self.fill_field_value("group_header", group.header)
        self.fill_field_value("group_footer", group.footer)

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        # select group
        wd.find_element_by_name("selected[]").click()
        # delete group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def modify_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        # select group
        wd.find_element_by_name("selected[]").click()
        # edit group
        wd.find_element_by_name("edit").click()
        # change
        self.fill_group_form(group)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
