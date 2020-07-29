# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="modifyfirst", middlename="editmiddle", nickname="editnick", lastname="editlast", title="contact", company="test", address="Moscow", homenumber="123",
                                             mobilenumber="8915", worknumber="8916", faxnumber="8917", email1="tuser@mail.ru", email2="tuser@mail.com", email3="tuser@mail.rucom", homepage="tuser.ru", address2="Russia", phone2="8920", notes="modify"))
    app.session.logout()
