# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_modify_contact(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.add(Contact(firstname="test", middlename="test", nickname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_edit = Contact(firstname="modifyfirst", middlename="editmiddle", nickname="editnick", lastname="editlast",
                      title="contact", company="test", address="Moscow", homephone="123", mobilephone="8915",
                      workphone="8916", fax="8917", email1="tuser@mail.ru", email2="tuser@mail.com",
                      email3="tuser@mail.rucom", homepage="tuser.ru", address2="Russia", secondaryphone="8920",
                      notes="modify")
    app.contact.modify_by_id(contact.id, contact_edit)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    contact.firstname = contact_edit.firstname
    contact.lastname = contact_edit.lastname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
