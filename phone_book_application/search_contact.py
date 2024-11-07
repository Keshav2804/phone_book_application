def search_contact(phone_book):
    name = input("Enter the name of the contact to search: ")
    if name in phone_book:
        print("{}:{}".format(name,phone_book[name]))
    else:
        print("Contact {} not found.".format(name))
