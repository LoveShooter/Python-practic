import requests
url = "https://yandex.ru"
page = requests.get(url)
urlStatus = page.status_code 

#print(page)
#print(urlStatus)
if ( urlStatus > 200 != 200 ):
    print("HTTP Status:",urlStatus, "BAD")
else:
    print ("HTTP Status:",urlStatus, "GOOD") 


    
try:
    page1 = requests.get(url)
except requests.exceptions.ConnectionError:
    r.status_code = "Connection refused"