import os
import shutil

print(dir(os))  # List all methots in module os

print("---------------------------------------------")

path = 'G:/OneDrive/coding/python/PythonPractice'
dir_list = os.listdir(path)  

print("List of directories and files before creation:") 
print(dir_list) 
print()


os.mkdir('testfolder2')
os.chdir('testfolder2')
pathNew = 'G:/OneDrive/coding/python/PythonPractice/testfolder2'

print("New Work directory is:")
print(os.getcwd()) # Show work dir
print()

with open('myfile.txt', 'w') as fp: # Create new file
    pass


dir_list = os.listdir(pathNew) 
print("List of directories and files after creation:") 
print(dir_list)
print()

newDir = input("Input name of new folder:")
os.mkdir(newDir) #Create new dir in current folder
os.chdir(newDir) #Change work dir
newPath = os.getcwd() 
print(newPath)
print()

source = "G:/OneDrive/coding/python/PythonPractice/testfolder2/myfile.txt"
destination = newPath

shutil.copy2(source, destination) # Copy file
