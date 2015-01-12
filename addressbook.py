Numbers=[]
Names=[]
option =0

while True:
    print "---------------------------------------"
    option = raw_input("Enter the number of the Option you want:"+
                "\n--------------------------"+
                "\n'1' To Add Contact"+
               "\n'2' To search contacts by Name\n'3' To search contacts by the Number"+
               "\n'4' To Edit the Contact\n'5' To list the Address book\n'6' To quit\n"+
                "----------------------------------------\n>")

    if option == "1":
        print "-------------"
        print "Add Contacts to address book!\n-------------"
        name = raw_input("Enter name :")
        Names.append(name)
        number = input("Enter number :")
        Numbers.append(number)
        
    elif option == "2":
        print "\nSearch for the contact by name\n--------------------"
     
        name = raw_input("Enter the name :")
        if name in Names:
            print "The Contact are listed Below"
            print "-----------------------------"
            index = Names.index(name)
            
            print "Name   :", Names[index]
            print "Number : ", Numbers[index]
         
         
        elif name not in Names:
            print "\nThis contact does not exist!!\n----------------------\n"
         
    elif option == "3":
        print "\nSearch Contact by phone number\n----------------------------"
        number = input("Enter the number :")
        if number in Numbers:
            print "\n---------------------------"
            print "The Contact are listed Below"
            index = Numbers.index(number)
            
         
            print "\nThe Number : ", Numbers[index]
            print "Belongs to :", Names[index]
            print "----------------------------"

        elif number not in Numbers:
            print "\nThis Contact Does Not Exist!!\n-------------------\n"
 
    elif option == "4":
        print "\nEdit the Contact!\n------------------\n"

        name = raw_input("Enter Contact Name to Edit:\n->")
        if name not in Names:
            print "\nThis Name Does not exist!\n"
         
        elif name in Names:
            index = Names.index(name)
            Names.remove(name)
            del Numbers[index]

     
            print "--------------------"
            print "Adding New Contact\n------------------\n"
            name = raw_input("Enter New Name :")
            Names.append(name)
            number =input("Enter New Number :")
            Numbers.append(number)
            print "\n----------------"
            print "Contact has been added!!\n--------------\n"
     
    elif option =="5":
        print "----------------------------"
        print "Printing the Address book\n-----------------------"

        for i in range(len(Names)):
            print str(Names[i]) + "........"+ str(Numbers[i])
        #print Names
        #print Numbers
        print "--------------------"
    elif option == "6":
        print "See ya later!"
        break

