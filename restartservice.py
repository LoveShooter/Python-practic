import requests
import subprocess

from urllib3 import disable_warnings, exceptions
disable_warnings(exceptions.InsecureRequestWarning)

# ENV
url = "https://yandex.ru"
page = requests.get(url, verify=False)
urlStatus = page.status_code

#print(page)
#print(urlStatus)

# Checking code of HTTP response
# If BAD status then Restart Service
if ( urlStatus > 200, urlStatus != 200 ):
    subprocess.run(['powershell', '-Command','Restart-Service -Name PowerBIReportServer'])
    print("HTTP Status:",urlStatus, "BAD. Service restarted!")
else:
    print ("HTTP Status:",urlStatus, "GOOD. No need Restart.") 


input("pause")