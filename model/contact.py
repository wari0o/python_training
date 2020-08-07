from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, nickname=None, lastname=None, title=None, company=None,
                 address=None, homenumber=None, mobilenumber=None, worknumber=None, faxnumber=None, email1=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, group=None, address2=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.nickname = nickname
        self.lastname = lastname
        self.title = title
        self.company = company
        self.address = address
        self.homenumber = homenumber
        self.mobilenumber = mobilenumber
        self.worknumber = worknumber
        self.faxnumber = faxnumber
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
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:s:s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
