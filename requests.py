import requests

r = requests.get('https://github.com')

stcode = r.status_code
if stcode == 200: print("Все ґуд")
if stcode == 404: print("Помилочка, нічого не знайдено")

find = requests.get('https://api.github.com/search/repositories', {'q': input("Вкажіть шукане: ")})
js = find.json()
n = -1
while 1:
    info = js['items'][n]
    print(info["html_url"])
    if js['items'][n] == js['items'][0]:
        break
    n -=1

#Василь Васильович Гриньків, група КІПЗс-2017
