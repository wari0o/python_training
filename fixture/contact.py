from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_by_index(0)

    def modify_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # edit first contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

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

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook.php") and len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=\"entry\"]"):
                lastname = element.find_elements_by_tag_name("td")[1].text
                firstname = element.find_elements_by_tag_name("td")[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)
