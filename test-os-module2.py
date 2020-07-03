import os

path = 'G:/OneDrive/coding/python/PythonPractice/testfolder/api_uploaded_files'


def createMultipleFolders():
    os.chdir(path)
    folders = ['2001','2002','2003', '2004', '2005'] 
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Folders", folder, "created successfully")
        else:
            print("Folders", folder, "already exists!")


if __name__ == '__main__':
    createMultipleFolders()