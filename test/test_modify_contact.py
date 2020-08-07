# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test", middlename="test", nickname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="modifyfirst", middlename="editmiddle", nickname="editnick", lastname="editlast",
                      title="contact", company="test", address="Moscow", homenumber="123", mobilenumber="8915",
                      worknumber="8916", faxnumber="8917", email1="tuser@mail.ru", email2="tuser@mail.com",
                      email3="tuser@mail.rucom", homepage="tuser.ru", address2="Russia", phone2="8920", notes="modify")
    contact.id = old_contacts[index].id
    app.contact.modify_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
