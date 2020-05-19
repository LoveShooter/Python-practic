import os
import shutil

path = 'G:/OneDrive/coding/python/PythonPractice/testfolder/api_uploaded_files'

print(dir(os))
dir_list = os.listdir(path) 

print("----------------------------------------------")
print("List of directories and files before creation:") 
print(dir_list) 
print()

filename = input("Input Filename to search:")
print(filename)

isfile = os.path.exists(path)  #Path exists - true\false 
print(isfile)


filePath = os.path.join(path, filename) #Create full path to file
print(filePath)
os.remove(filePath)  #Remove file
print(dir_list)