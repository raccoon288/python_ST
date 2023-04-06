from model.group import Group
from model.contact import Contact
from random import randrange


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    index_contacts = randrange(len(db.get_contact_list()))
    index_groups = randrange(len(db.get_group_list()))
    app.contact.add_contact_to_group(contacts[index_contacts], groups[index_groups])


def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))


