def edit_contact(phone_book):
    name = input("Enter the name of the contact to edit: ")
    if name in phone_book:
        new_phone = input("Enter the new phone number: ")
        phone_book[name] = new_phone
        print("Contact {} updated successfully.".format(name))
    else:
        print("Contact {} not found.".format(name))
