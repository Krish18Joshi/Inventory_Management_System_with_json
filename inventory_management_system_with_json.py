# -*- coding: utf-8 -*-
"""Inventory Management System with JSON.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1plpZ3kB_C2DsrPAhtyvr9kW7rjm9ZAQS
"""

import json
import time

# Importing Inventory data from Record.json file
fd = open('Record.json','r')
js = fd.read()
fd.close()

# Converting String data to Dictionary
record = json.loads(js)

# Displaying Menu
print("--------------------MENU---------------------")
for key in record.keys():
    print(key, record[key]['Name'], record[key]['Price'], record[key]['Qn'])
print("---------------------------------------------")
print('')

# Taking Inputs from the user about their details and purchase
ui_name = str(input("Enter your name    : "))
ui_mail = str(input("Enter Mail ID      : "))
ui_ph   = str(input("Enter Phone No     : "))
ui_pr   = str(input("Enter product ID   : "))
ui_qn   = int(input("Enter Quantity     : "))

print("---------------------------------------------")
print('')
# If we're having equal or more quantity then the user wants
if (record[ui_pr]['Qn'] >= ui_qn):

    print("Name      : ", record[ui_pr]["Name"])
    print("Price (Rs): ", record[ui_pr]["Price"])
    print("Quantity  : ", ui_qn)
    print("---------------------------------------------")
    print("Billing   : ", ui_qn * record[ui_pr]["Price"], "Rs")
    print("---------------------------------------------")

    # Updating Inventory in Dictionary
    record[ui_pr]['Qn'] = record[ui_pr]['Qn'] - ui_qn

    # Generating CSV Transection Detail
    sale = ui_name+","+ui_mail+","+ui_ph+","+ui_pr+","+record[ui_pr]["Name"]+","+str(ui_qn)+","+str(record[ui_pr]["Price"])+","+str(ui_qn * record[ui_pr]["Price"])+","+time.ctime()+"\n"
# If we're less quantity then the user wants
else:

    print("Sorry, We're not having enough quanity of product in our Inventory.")
    print("We're only having " + str(record[ui_pr]['Qn']) + " quantity.")
    print("---------------------------------------------")

    ch == str(raw_input("Press Y to purchase: "))

    # If user wants to purchase the whole quantity for that product
    if(ch == "Y" or ch == 'y'):

        print("---------------------------------------------")
        print("Name      : ", record[ui_pr]["Name"])
        print("Price (Rs): ", record[ui_pr]["Price"])
        print("Quantity  : ", record[ui_pr]['Qn'])
        print("---------------------------------------------")
        print("Billing   : ", record[ui_pr]['Qn'] * record[ui_pr]["Price"], "Rs")
        print("---------------------------------------------")

        # Updating Inventory in Dictionary
        record[ui_pr]['Qn'] = 0

        # Generating CSV Transection Detail
        sale = ui_name+","+ui_mail+","+ui_ph+","+ui_pr+","+record[ui_pr]["Name"]+","+str(record[ui_pr]['Qn'])+","+str(record[ui_pr]["Price"])+","+str(record[ui_pr]['Qn'] * record[ui_pr]["Price"])+","+time.ctime()+"\n"

    # If user pressed anything except Y or y
    else:
        print("Thanks!")
# Converting Inventory Dictionary to String
js = json.dumps(record)

# Updating Inventory and Saving in to my Records.json
fd = open('Record.json','w')
fd.write(js)
fd.close()

# Adding Transection on Sales File
fd = open('Sales.txt','a')
fd.write(sale)
fd.close()

print('')
print("---------------------------------------------")
print("  Thanks for your order, Inventory Updated!  ")
print("---------------------------------------------")

"""#Data

{"1005": {"Price": 650, "Name": "Blueberry Cake", "Qn": 3}, "1004": {"Price": 550, "Name": "Chocolate Cake", "Qn": 6}, "1003": {"Price": 2, "Name": "Candy", "Qn": 500}, "1002": {"Price": 20, "Name": "Bar-One", "Qn": 0}, "1001": {"Price": 10, "Name": "5 Star", "Qn": 188}}
"""