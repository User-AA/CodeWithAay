import os
import time
from colorama import Fore

password = "Password123"
what_is_your_password = "Password123"

print (Fore.GREEN + "How old are you?")
age = input("-->")

if age > "13":
  print ("you are eligable to use this program.")
  time.sleep(2)
  os.system('clear') 
  
if age < "13":
  print ("You are not eligable to use this program.")
  time.sleep(2)
  os.system('clear') 
  exit()
  
#Sign in
print ("SIGN IN...")
what_is_your_password = input("-->  ")
time.sleep(1.5)


#Checks if password is correct
if password == what_is_your_password:
  print ("-CORRECT-")
  time.sleep(1.5)
  os.system('clear') 
  print ("Which file would you like to open?")
  time.sleep(0.5)
  print ("File chioces:")
  print ("file A")
  print ("file B")
  print ("file C")
  print ("Which file would you like to open?")
  file_choice = input ("-->  ")
  
  for i in range(1,3):
    os.system('clear') 
    print ("wait.")
    time.sleep(1.5)
    os.system('clear') 
    print ("wait..")
    time.sleep(1.5)
    os.system('clear') 
    print ("wait...")
    time.sleep(1.5)
    os.system('clear') 
    time.sleep(1.5)
  time.sleep(1.5)
  os.system('clear') 

  if file_choice == "file A":
    x = open("File_A.txt", "+a")
  if file_choice == "file B":
    y = open("File_B.txt", "+a")
  if file_choice == "file D":
    z = open("File_D.txt", "+a")

    
#If password is wrong, gives more chances
elif password == password:
  if password == password:
    print (Fore.RED + "-INCORRECT-")
    time.sleep(1.5)
    print ("Try again please.")
    time.sleep(1.5)
    os.system('clear') 
    print ("SIGN IN...")
    what_is_your_password = input (Fore.GREEN + "-->  ")
    time.sleep(1.5)

    
#Opens file
  if password == what_is_your_password:
    print ("-CORRECT-")
    time.sleep(1.5)
    os.system('clear') 
    print ("Which file would you like to open?")
    time.sleep(0.5)
    print ("File chioces:")
    print ("file A")
    print ("file B")
    print ("file C")
    print ("Which file would you like to open?")
    file_choice = input ("-->  ")
  for i in range(1,3):
    os.system('clear') 
    print ("wait.")
    time.sleep(1.5)
    os.system('clear') 
    print ("wait..")
    time.sleep(1.5)
    os.system('clear') 
    print ("wait...")
    time.sleep(1.5)
    os.system('clear') 
    time.sleep(1.5)
  time.sleep(1.5)
  os.system('clear') 

  if file_choice == "file A":
    x = open("File_A.txt", "+a")
  if file_choice == "file B":
    y = open("File_B.txt", "+a")
  if file_choice == "file D":
    z = open("File_D.txt", "+a")

    
#End code
print ("Your file has been opened.")
time.sleep(1.5)


#Close file code
print ("Would you like to close all files?")
print ("y/n")

close_file = input ("-->  ")

y = True

if close_file == "y":
   x,y,z.close()

    
#NOTES-
# - Delete file w code
