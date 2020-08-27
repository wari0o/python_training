from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, nickname=None, lastname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email1=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, group=None, address2=None, secondaryphone=None, notes=None, id=None,
                 all_email_from_home_page=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.nickname = nickname
        self.lastname = lastname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.group = group
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address,
                                                     self.homephone, self.mobilephone, self.workphone,
                                                     self.secondaryphone, self.email1, self.email2, self.email3,
                                                        self.all_phones_from_home_page, self.all_email_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname \
               and self.address == other.address \
               and self.homephone == other.homephone \
               and self.mobilephone == other.mobilephone \
               and self.workphone == other.workphone \
               and self.secondaryphone == other.secondaryphone \
               and self.email1 == other.email1 \
               and self.email2 == other.email2 \
               and self.email3 == other.email3 \
               and self.all_phones_from_home_page == other.all_phones_from_home_page \
               and self.all_email_from_home_page == other.all_email_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
