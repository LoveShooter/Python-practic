import requests
url = "URL"
page = requests.get(url)
urlStatus = page.status_code 
#print(urlStatus)
if ( urlStatus != 200 ):
    print("HTTP Status:",urlStatus, "BAD")
else:
    print ("HTTP Status:",urlStatus, "GOOD") 