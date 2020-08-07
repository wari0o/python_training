# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="tuserfirst", middlename="tusermiddle", nickname="tusernick", lastname="tuserlast",
                      title="contact", company="test", address="Moscow", homenumber="123", mobilenumber="8915",
                      worknumber="8916", faxnumber="8917", email1="tuser@mail.ru", email2="tuser@mail.com",
                      email3="tuser@mail.rucom", homepage="tuser.ru", bday="2", bmonth="January", byear="1990",
                      aday="16", amonth="July", ayear="2020", group="[none]", address2="Russia", phone2="8920",
                      notes="none")
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
