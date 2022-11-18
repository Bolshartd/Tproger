import os

login = os.getlogin()
print (login)

current_dir = os.getcwd()
print (current_dir)

list_dir = os.listdir(current_dir)
print (list_dir)