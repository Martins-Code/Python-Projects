def main():
    print("Welcome to email Slicer ")
    print("")

    email = input("Enter Your Email: ")
    string_split = '@'
    string_split_2 = '.'
    if string_split in email and string_split_2 in email:
        (username, domain) = email.split("@")
        (domain, extension) = domain.split(".")
        print("Username: ", username)
        print("Domain: ", domain)
        print("Extension: ", extension)
    else:
        print("Invalid Email")


main()
