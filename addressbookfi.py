import json
import sys

#initialize empty dictionary
phone_book = {}

#initialize file object and load txt data
f = open('address_book.txt', 'r')

#load txt data into dictionary
phone_book=json.load(f)

#close file
f.close()

def clear():
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[H')
    sys.stdout.flush()

#fucntion for adding to dictionary
def add(**kwargs):
    phone_book[name_input]=phone_input
    print '%s has been added to address book' % name_input
    save()
    
#function for printing out dictionary
def listy():
    print ''
    print "Contacts in Phone Book:"
    for (key) in sorted(phone_book.keys()):
#%-20s will have 20 spaces min
        print '%-16s: %s' % (key, phone_book[key])
#function for removing an entry from dictionary
def remove():
    x=raw_input('Enter the name of the entry you want to delete: ')
    if x in phone_book:
        del phone_book[x]
        print '%s has been removed from address book' % x
        save()
    else:
        print "did not find contact in address book, please try again!"
        remove()

#function for saving to the txt file
def save():
    f = open('address_book.txt', 'w')
    json.dump(phone_book, f)
    f.close()
print 'Contact has been saved to address book'


clear()
print 'My address book.'

#main loop
while True:
    print ''
    input1=raw_input('What would you like to do? to do? (add, remove, list, quit) ') 

    if input1=='add':
        name_input=raw_input('Name: ')
        phone_input=raw_input('Phone number: ')
        add(name_input='phone_input')

    elif input1=='list':
        listy()

    elif input1=='remove':

        listy()
        print ''
        remove()

    elif input1=='quit':
        print 'bye now!'
        print ''
        break

    else:
        print "Incorrect entry, please try again."
