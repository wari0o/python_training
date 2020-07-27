# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="editfirst", middlename="editmiddle", nickname="editnick", lastname="editlast", title="contact", company="test", address="Moscow", homenumber="123",
                            mobilenumber="8915", worknumber="8916", faxnumber="8917", email1="tuser@mail.ru", email2="tuser@mail.com", email3="tuser@mail.rucom", homepage="tuser.ru", bday="3",
                            bmonth="April", byear="1990", aday="15", amonth="May", ayear="2020", group="[none]", address2="Russia", phone2="8920", notes="edit"))
    app.session.logout()