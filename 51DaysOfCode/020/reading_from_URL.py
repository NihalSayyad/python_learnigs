import requests # importing the request module

url = 'https://api.thecatapi.com/v1/breeds' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
#print(response.headers)     # headers information
#print(response.text) # gives all the text from the page

for i in response.json():
    print(f"-------{i['name']}--------")
    weights = i['weight']['imperial'].split(' - ')
    x = [int(i) for i in weights]
    print(f"avg weight : {sum(x)/len(x)}")

