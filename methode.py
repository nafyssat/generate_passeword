

import random
import string


def generate_password(lent):
    # get the password
    password = ""
    for i in range(lent):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password