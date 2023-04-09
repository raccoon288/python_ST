from model.group import Group
from model.contact import Contact
from random import randrange


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    index_contacts = randrange(len(db.get_contact_list()))
    index_groups = randrange(len(db.get_group_list()))
    contacts_in_group = orm.get_contacts_in_group(groups[index_groups])
    if contacts[index_contacts] in contacts_in_group:
        app.contact.delete_contact_from_group(contacts[index_contacts], groups[index_groups])
    app.contact.add_contact_to_group(contacts[index_contacts], groups[index_groups])
    contacts_in_group = orm.get_contacts_in_group(groups[index_groups])
    assert contacts[index_contacts] in contacts_in_group


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    index_contacts = randrange(len(db.get_contact_list()))
    index_groups = randrange(len(db.get_group_list()))
    contacts_not_in_group = orm.get_contacts_not_in_group(groups[index_groups])
    if contacts[index_contacts] in contacts_not_in_group:
        app.contact.add_contact_to_group(contacts[index_contacts], groups[index_groups])
    app.contact.delete_contact_from_group(contacts[index_contacts], groups[index_groups])
    contacts_not_in_group = orm.get_contacts_not_in_group(groups[index_groups])
    assert contacts[index_contacts] in contacts_not_in_group

