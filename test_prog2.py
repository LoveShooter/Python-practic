# Checking return code of running PS cmd 
checkCode = serviceRestart.returncode
print(checkCode)
if checkCode!=0:
    print("Error")
else:
    print("Success!")

