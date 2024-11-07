def delete_contact(phone_book):
    name = input("Enter the name of the contact to delete: ")
    if name in phone_book:
        del phone_book[name]
        print("Contact {} deleted successfully.".format(name))
    else:
        print("Contact {} not found.".format(name))
