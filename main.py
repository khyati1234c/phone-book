phonebook={}
def add_contact():
    name=input("enter the contact name :")
    if name in phonebook:
        print("contact already exists")
    else:
        ph=input("enter the phone number")
        phonebook[name]=ph
        print("contact added successfuly")

def searchcontact():
    name=input("enter the contact to search:")
    if name in phonebook:
        print(f"{name} : {phonebook[name]}")
    else:
        print("contact not found")

def updatecontact():
    name=input("enter the contact name to update: ") 
    if name in phonebook:
        number=input("enter the new number: ")
        phonebook[name]=number
        print("contact added successfuly")
    else:
        print("contact not found")

def deletecontact():
    name=input("enter the contact to delete")
    if name in phonebook:
        del phonebook[name]
        print("contact deleted successfuly")
    else:
        print("contact not deleted")

def displaycontact():
    if phonebook:
        print("\n------ Contact List ------")
        for name,number in phonebook.items():
            print(f"{name} : {number}")
        print("--------------------------")

while True:

    print("\n--- Phone Book Menu ---")

    print("1. Add Contact")

    print("2. Search Contact")

    print("3. Update Contact")

    print("4. Delete Contact")

    print("5. Display All Contacts")

    print("6. Exit")

    ch=input("enter your choice :")

    if ch=="1":
        add_contact()

    elif ch=="2":
        searchcontact()
    elif ch=="3":
        updatecontact()
    elif ch=="4":
        deletecontact()
    elif ch=="5":
        displaycontact()
    elif ch=="6":
        break