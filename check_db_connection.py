import pymysql.cursors
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    list = db.get_contact_list()
    for l in list:
        print(l)
finally:
    pass
    # db.destroy()
