from model.group import Group
import random
import string


constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name1", header="header1", footer="footer1")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    random_len = random.randrange(maxlen)
    random_line = [random.choice(symbols) for i in range(random_len)]
    return prefix + "".join(random_line)


testdata = [
           Group(name=name, header=header, footer=footer)
           for name in ["", random_string("name", 10)]
           for header in ["", random_string("header", 20)]
           for footer in ["", random_string("footer", 20)]
           ]
