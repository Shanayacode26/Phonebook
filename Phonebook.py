import sys
def initial_phonebook():
    rows,cols=int(input("Please Enter Desired Number of Contacts: ")),5
    phonebook=[]
    print(phonebook)
    for i in range(rows):
        print("\nEnter Contact %d Details In The Following Order(ONLY): "%(i+1))
        print("NOTE:* Indicates Mandotary Fields")
        print("................................................................")
        temp=[]
        for s in range(cols):
            if s==0:
                temp.append(str(input("Enter Your Name*: ")))
                if temp[s]=="" or temp[s]==" ":
                    sys.exit("Name Is a Mandatory Field,Exiting Due to Blank Field")
            if s==1:
                temp.append(int(input("Enter Your Phone Number*: ")))
            if s==2:
                temp.append(str(input("Enter Your Email Address: ")))
                if temp[s]=="" or temp[s]==" ":
                    temp[s]=None               
            if s==3:
                temp.append(str(input("Enter Your Date Of Birth(DD/MM/YYYY): ")))
                if temp[s]=="" or temp[s]==" ": 
                    temp[s]=None
            if s==4:
                temp.append(str(input("Enter Your Catagory(Family/Friends/Work/Other): ")))
                if temp[s]=="" or temp[s]==" ":
                    temp[s]=None
        phonebook.append(temp)
    print(phonebook)
    return(phonebook)
def menu():
    print("*******************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice=int(input("Please Enter Your Choice: "))
    return choice
def add_contact(pb):
    dip=[]
    for i in range(len(pb[0])):
        if i==0:
            dip.append(str(input("Enter Name: ")))
        if i==1:
            dip.append(int(input("Enter Phone Number: ")))
        if i==2:
            dip.append(str(input("Enter Email Address: ")))
        if i==3:
            dip.append(str(input("Enter Date of Birth(DD/MM/YYYY): ")))
        if i==4:
            dip.append(str(input("Enter Catagory(Family/Friends/Work/Other): ")))
    pb.append(dip)
    return pb                    