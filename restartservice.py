import requests
import subprocess

# ENV
url = "https://yandex.ru"
page = requests.get(url)
urlStatus = page.status_code 


#print(page)
#print(urlStatus)

# Checking code of HTTP response
# If BAD status then Restart Service
if ( urlStatus > 200 != 200 ):
    serviceRestart = subprocess.run(['powershell', '-Command','Restart-Service -Name spooler'])
    print("HTTP Status:",urlStatus, "BAD. Service restarted!")
else:
    print ("HTTP Status:",urlStatus, "GOOD. No need Restart.") 


input("pause")