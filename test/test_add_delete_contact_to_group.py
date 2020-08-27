from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="test", lastname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    dbconnect = ORMFixture(host=db.host, name=db.name, user=db.user, password=db.password)
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = dbconnect.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        app.contact.add(Contact(firstname="test", lastname="test"))
        contacts = dbconnect.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_to_group(contact.id, group.id)
    contacts_in_group = dbconnect.get_contacts_in_group(Group(id=group.id))
    dbconnect.db.provider = dbconnect.db.schema = None
    assert check(contact, contacts_in_group) is True


def test_del_contact_from_group(app, db):
    dbconnect = ORMFixture(host=db.host, name=db.name, user=db.user, password=db.password)
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = dbconnect.get_contacts_in_group(group)
    while len(contacts) == 0:
        test_add_contact_to_group(app, db)
        groups = db.get_group_list()
        group = random.choice(groups)
        contacts = dbconnect.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_from_group(contact.id, group.id)
    contacts_not_in_group = dbconnect.get_contacts_not_in_group(Group(id=group.id))
    dbconnect.db.provider = dbconnect.db.schema = None
    assert check(contact, contacts_not_in_group) is True


def check(contact, contacts_in_group):
    for row in contacts_in_group:
        if row.id == contact.id:
            return True
    return False
