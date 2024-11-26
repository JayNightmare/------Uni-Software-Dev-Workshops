import requests

resposne = requests.get('https://jsonplaceholder.typicode.com/posts')

if resposne.status_code == 200:
    print(resposne.text)