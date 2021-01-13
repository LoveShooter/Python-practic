import requests
url = "https://yandex.ru"
page = requests.get(url)
urlStatus = page.status_code 
#print(page)
#print(urlStatus)
if ( urlStatus != 200 ):
    print("HTTP Status:",urlStatus, "BAD")
else:
    print ("HTTP Status:",urlStatus, "GOOD") 