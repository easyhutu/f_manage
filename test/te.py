"""
CREATE: 2018/5/18
AUTHOR:　HEHAHUTU
"""
import requests

data = {'username': 'meng', 'password': '123456'}

html = requests.post('http://localhost:5000/x/config', json=data)
print(html.json())