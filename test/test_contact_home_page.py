from random import randrange
from model.contact import Contact


def test_contact_info_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_all_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_all_phones(contact_from_edit_page)


def test_contact_info_on_home_page_all_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_db) == app.contact.count()
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_home_page[i].all_emails_from_home_page == app.contact.merge_all_emails(contacts_from_db[i])
        assert contacts_from_home_page[i].all_phones_from_home_page == app.contact.merge_all_phones(contacts_from_db[i])
