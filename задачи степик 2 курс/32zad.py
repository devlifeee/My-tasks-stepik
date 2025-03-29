import requests

with open('685 (1).txt', 'r') as f:
  url = f.read().strip()

response = requests.get(url)
if response.status_code == 200:
  lines = response.text.splitlines()
  print(len(lines))
else:
  print("Ошибка: Не удалось скачать файл.")