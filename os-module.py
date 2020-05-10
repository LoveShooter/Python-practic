import os
print(dir(os))  # List all methots in module os

print("---------------------------------------------")

print(os.getcwd()) # Show work dir

print("---------------------------------------------")
print(os.listdir()) # List dir in work dir

os.chdir('testfolder')  # Change dir
print(os.getcwd()) # Show work dir

#os.mkdir('testdir') # Create dir in working dir
print(os.listdir()) 

#os.makedirs('level1dir/level2dir') #Create 2 dirs recursive
print(os.listdir())

#os.rmdir('testdir') #Delete 1 dir in work dir
print(os.listdir())

os.removedirs('level1dir/level2dir')
print(os.listdir())