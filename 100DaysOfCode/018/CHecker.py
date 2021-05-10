import  urllib
import requests
import copy
import time

base_request_header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        }

request_header = copy.deepcopy(base_request_header)
request_header["Authorization"] = f"Bearer nihal"

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=413102&date=11-05-2021"
response = requests.get(url=url, headers=request_header)
counter = 0
while response.status_code == 200 and response.json()['sessions'] == []:
    print(response.status_code)
    data = response.json()
    print(data['sessions'])
    counter += 1

    response = requests.get(url=url, headers=request_header)

    if counter == 10:
        break
    time.sleep(60)
else:
    data = response.json()
    print(data['sessions'])
