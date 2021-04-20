import requests

r = requests.get('https://github.com')

rcode = r.status_code
if rcode == 200: print("Все ґуд")
if rcode == 404: print("Помилочка, нічого не знайдено")

s = {'q': input("Вкажіть шукане: ")}
r = requests.get('https://github.com/search', s)
print(r.url)

#Василь Васильович Гриньків, група КІПЗс-2017
