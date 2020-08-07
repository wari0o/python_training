# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test", middlename="test", nickname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="modifyfirst", middlename="editmiddle", nickname="editnick", lastname="editlast",
                      title="contact", company="test", address="Moscow", homenumber="123", mobilenumber="8915",
                      worknumber="8916", faxnumber="8917", email1="tuser@mail.ru", email2="tuser@mail.com",
                      email3="tuser@mail.rucom", homepage="tuser.ru", address2="Russia", phone2="8920", notes="modify")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
