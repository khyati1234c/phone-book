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


        

