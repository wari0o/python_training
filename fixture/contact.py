from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()

    def delete_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # edit first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit contact creation
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        # upload image
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys("C:\\Users\\Wari\\Pictures24569707_60x60.png")
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homenumber)
        self.change_field_value("mobile", contact.mobilenumber)
        self.change_field_value("work", contact.worknumber)
        self.change_field_value("fax", contact.faxnumber)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # fill date
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        # # wd.find_element_by_xpath("//option[@value='1']").click()
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        # # wd.find_element_by_xpath("//option[@value='January']").click()
        # wd.find_element_by_name("theform").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys(contact.byear)
        # wd.find_element_by_name("aday").click()
        # wd.find_element_by_name("aday").click()
        # wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        # # wd.find_element_by_xpath("(//option[@value='16'])[2]").click()
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        # # wd.find_element_by_xpath("(//option[@value='July'])[2]").click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys(contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
