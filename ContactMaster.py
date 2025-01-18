#python program for a contact dictionary

def add_contacts():
    name=input("ENTER NAME: ")
    phone=input("ENTER PHONE NUMBER: ")
    if name in contactlist:
        print("This contacts exists already")
    else:
        contactlist[name]=phone
        print("Contact added successfully")

def del_contacts():
    name = input("ENTER NAME: ")
    if name in contactlist:
        del contactlist[name]
        print("Contact deleted successfully")
    else:
        print("This contact doesn't exists")

def update_contacts():
    name = input("ENTER NAME: ")
    for contact in contactlist:
        if name in contactlist:
            phone = input("Enter new mobile number")
            contactlist[name] = phone
            print("Contact updated successfully")
            break
        else:
            print("contacts can't find out")


def search_contacts():
    name = input("ENTER NAME: ")
    if name in contactlist:
            print("Contact found")
            print(name)
    else:
            print("Contact not found")

def display_contacts():
    if contactlist=={}:
        print("There are no contacts")
    else:
        print("Contact list")
        for name,phone in contactlist.items():
            print(name,phone)
contactlist = {}

while True:
    print("\n .......Contact list Menu.........")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("4. Search contact")
    print("5. Display contact")
    print("6.exit")

    choice=int(input("Enter your choice(1-6)::"))
    if choice == 1:
        add_contacts()

    elif choice==2:
        del_contacts()

    elif choice==3:
        update_contacts()

    elif choice==4:
        search_contacts()

    elif choice==5:
        display_contacts()

    elif choice==6:
        print("good bye")
        break

    else:
        print("Invalid choice")
