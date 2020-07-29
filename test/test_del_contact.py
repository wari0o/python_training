from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test", middlename="test", nickname="test"))
    app.contact.delete_first()
