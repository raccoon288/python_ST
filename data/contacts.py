from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    random_len = random.randrange(maxlen)
    random_line = [random.choice(symbols) for i in range(random_len)]
    return prefix + "".join(random_line)


def random_phones(prefix, maxlen):
    symbols = string.digits + "[" + "(" + ")" + "-" + "]"
    random_len = random.randrange(maxlen)
    random_line = [random.choice(symbols) for i in range(random_len)]
    return prefix + "".join(random_line)


def random_emails(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "-" + "_"
    random_len = random.randrange(maxlen)
    random_line = [random.choice(symbols) for i in range(random_len)]
    return prefix + "".join(random_line) + "@" + "".join(random_line) + ".ru"


def random_images():
    images = ["test_image.jpg", "test_image2.jpg", "test_image3.jpg", "test_image4.jpg", "test_image5.jpg"]
    index = random.randrange(5)
    return images[index]


testdata = [
            Contact(firstname="",
                    middlename="",
                    lastname="",
                    nickname="",
                    image_name=None,
                    title="",
                    company="",
                    address="",
                    home_number="",
                    mobile_number="",
                    work_number="",
                    fax="",
                    email="",
                    email2="",
                    email3="",
                    homepage="",
                    bday="",
                    bmonth="",
                    byear="",
                    aday="",
                    amonth="",
                    ayear="",
                    address2="",
                    phone2="",
                    notes="")
            ] + \
            [
             Contact(firstname=random_string("firstname", 10),
                     middlename=random_string("middlename", 10),
                     lastname=random_string("lastname", 10),
                     nickname=random_string("nickname", 10),
                     image_name=random_images(),
                     title=random_string("title", 10),
                     company=random_string("company", 10),
                     address=random_string("address", 10),
                     home_number=random_phones("home_number", 15),
                     mobile_number=random_phones("mobile_number", 15),
                     work_number=random_phones("work_number", 15),
                     fax=random_phones("fax", 15),
                     email=random_emails("email", 10),
                     email2=random_emails("email2", 10),
                     email3=random_emails("email3", 10),
                     homepage=random_string("homepage", 10),
                     bday=random.randrange(1, 32),
                     bmonth=random.randrange(1, 13),
                     byear=random.randrange(1, 3000),
                     aday=random.randrange(1, 32),
                     amonth=random.randrange(1, 13),
                     ayear=random.randrange(1, 3000),
                     address2=random_string("address2", 10),
                     phone2=random_phones("phone2", 15),
                     notes=random_string("notes", 10))
             for i in range(5)
            ]
