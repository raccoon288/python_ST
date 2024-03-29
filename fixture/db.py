import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """
                select id, 
                       firstname, 
                       lastname, 
                       home, 
                       mobile, 
                       work, 
                       phone2,
                       email,
                       email2,
                       email3 
                from addressbook 
                where deprecated='0000-00-00 00:00:00'
                """
            )
            for row in cursor:
                (id, firstname, lastname, home_number,
                 mobile_number, work_number, phone2,
                 email, email2, email3) = row
                contact_list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                            home_number=home_number, mobile_number=mobile_number,
                                            work_number=work_number, phone2=phone2,
                                            email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
