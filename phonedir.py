#!/usr/bin/env python3

import csv
import os
phones = []
name_pos = 0
phone_pos = 1
phone_header = ['Name','Phone Number']

def proper_menu_choice(which):
  if not which.isdigit():
    print(" "+ which+ " need to be the number of a phone")
    return False
  which = int(which)
  if which < 1  or which > len(phones):
    print(" " + str(which)+ " needs to be the number of phone!")
    return False
  return True

def delete_phone(which):
  if not proper_menu_choice(which):
    return 
  which = int(which)
  del phones[which -1]
  print("Deleted phone a", which)

def edit_phone(which):
  if not proper_menu_choice(which):
    return
  which = int(which)

  phone = phones[which -1]
  print("Enter a data for a new phone, Press <enter> to leave unchanged")

  print(phone[name_pos])
  newname = input("Enter the new name to change or press enter")
  if newname == "":
    newname = phone[name_pos]
  
  print(phone[phone_pos])
  newphone_num = input("Enter the new phone to change or press enter")
  if newphone_num == "":
    newphone_num = phone[phone_pos]
  phone = [newname, newphone_num]
  phones[which - 1] = phone

  

def save_phone_list():
  f = open("myphones.csv", 'w', newline= '')
  for item in phones:
    csv.writer(f).writerow(item)
  f.close()
  print("Loading")

def create_phone():
  print("Adding a phone")

def reorder_phone():
  #print(phones)
  phones.sort()
  show_phones()
  #print(phones)

def load_phone_list():
  if os.access("myphones.csv", os.F_OK):
    f = open("myphones.csv")
    for row in csv.reader(f):
      phones.append(row)
    f.close()
  

def show_phones():
  show_phone(phone_header, "")
  index = 1
  for phone in phones:
    show_phone(phone, index)
    index += 1
  print()

def show_phone(phone, index):
  outputstr = "{0:>3} {1:<20} {2:>16}"
  print(outputstr.format(index, phone[name_pos],phone[phone_pos]))

def create_phone():
  print("Enter the data for new phone")
  newname = input("Enter name: ")
  newphone_num = input("Enter phone number: ")
  phone = [newname, newphone_num]
  phones.append(phone)
  print()

def menu_choice():
  print("Choose one of the following options?")
  print("  s)Show")
  print("  n)New")
  print("  d)Delete  ")
  print("  e)Edit")
  print("  q)Quit")
  print("  r)Reorder")
  choice = input("Choise: ")
  if choice.lower() in ['n', 'd', 's', 'e', 'q', 'r']:
    return choice.lower()
  else:
    print(choice+"?"+ " That is an invalid options!!!")
    return None

def main_loop():
  load_phone_list()
  while True:
    choice = menu_choice()
    if choice == None:
      continue
    if choice == 'q':
      print("Exiting..")
      break
    elif choice == 'n':
      create_phone()

    elif choice == 'd':
      which = input("Which items do you want to delete? ")
      print("which is", which)
      delete_phone(which)

    elif choice == 's':
      show_phones()
    elif choice == 'e':
      which = input("Which item do you want to edit? ")
      print("Which is", which)
      edit_phone(which)

    elif choice == 'r':
      reorder_phone()
    else:
      print("Invalid choice.")
  save_phone_list()

if __name__== "__main__":
  main_loop()

