from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen, suffix):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + suffix


def random_phone(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 40), email1=random_email(10, "@email.com"),
            email2=random_email(10, "@email.com"), email3=random_email(10, "@email.com"),
            homephone=random_phone(10), mobilephone=random_phone(10), workphone=random_phone(10),
            secondaryphone=random_phone(10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
