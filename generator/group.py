from model.group import Group
import random
import string
import os
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    random_len = random.randrange(maxlen)
    random_line = [random.choice(symbols) for i in range(random_len)]
    return prefix + "".join(random_line)


testdata = [Group(name="", header="", footer="")] + \
           [
            Group(name=random_string("name", 10),
                  header=random_string("header", 20),
                  footer=random_string("footer", 20))
            for i in range(n)
           ]

abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)
file = os.path.join(dir_name, "..", f)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
