def add_contact(phone_book):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    phone_book[name] = phone
    print("Contact {} added successfully.".format(name))
