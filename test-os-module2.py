import os

path = 'G:/OneDrive/coding/python/PythonPractice/testfolder/api_uploaded_files'

folders = ['2001','2002','2003', '2004', '2005'] 

def createMultipleFolders():
    os.chdir(path)
    folders = ['2001','2002','2003', '2004', '2005'] 
    for folder in folders:
        if os.path.exists(folder):
            response = {"Foldes already exists!"}
        else:
            os.mkdir(folder)
            response = {"Folders created successfully"}
    #return print(response)