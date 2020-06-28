import os
import shutil

path = 'G:/OneDrive/coding/python/PythonPractice/testfolder/api_uploaded_files'

#print(dir(os))
dir_list = print(os.listdir(path))
os.chdir(path)

print("--------New path--------")
print(os.getcwd())

folderName = 'test2'
os.mkdir(folderName)

print("----------Path join---------")
pathNew  = print(os.path.join(path, folderName))

print("----------Revert slashes--------")
pathNew2 = os.path.abspath(folderName)
print(pathNew2)

os.chdir(pathNew2)

print("------New path------")
print(os.getcwd())

#dirName = input("Enter dir name:")   
#os.mkdir(dirName)   # Make new dir


print("----------------------------------------------")
print("List of directories and files before creation:") 
print(os.listdir(path))
print()

#dirDelete = input("Folder name for delete:")
#for dir in os.listdir(path):
#    shutil.rmtree(path, ignore_errors=True)    #Delete dir

#filename = input("Input Filename to search:")
#print(filename)

isfile = os.path.exists(path)  #Path exists - true\false 
print(isfile)  #True\False


#filePath = os.path.join(path, filename) #Create full path to file
#print(filePath)
#os.remove(filePath)  #Remove file
