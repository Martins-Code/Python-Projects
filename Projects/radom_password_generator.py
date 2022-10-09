import string, random

chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    password_length = int(input("Length of password: "))
    random.shuffle(chars)
    password = []
    for x in range(password_length):
        password.append(random.choice(chars))

    random.shuffle(password)

    password = "".join(password)

    print(password)


generate_password()
