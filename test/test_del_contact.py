from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test", middlename="test", nickname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
