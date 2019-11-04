import requests

url = "http://118.31.170.46:8000/api/tempimage?v=3.0.0"
headers = {
    "cookie": "laravel_session=eyJpdiI6IkpQYmt2eW9EeURQQTd0dmcwY09TcVE9PSIsInZhbHVlIjoiOGhDQW1aZjN"
              "KVXVTSldTdGM0TjFaWTZKbW9zZFI1aDh2UUZrdk1ZRUF5VmY4d3RJUUZoQkNiQUZhR041cDNpYyIsIm1hYy"
              "I6IjZmN2IwNmNhNWFhMGU0YjllYmQ1ZmU3NTVjMDM4OGE0NzI0Zjg1ZDZiNjQyNWE0NDNkNmUzODQzNmU0ZmY1M2QifQ%3D%3D;",
    "Accept": "application/json",
    # "Content-Type": "multipart/form-data; boundary=8b68adfb-2099-428b-8784-7457f1caee7e",
    "User-Agent": "okhttp/3.11.0"
}
params = {
    '_token': "PqYahHqFMEmPpkI42dNVUHocxGQfusZZQkMdkTui"
}
img = open(r"C:\Users\guofei.sun\Desktop\测试头像\1836c9daf4b1aba35f5ed7b68b7d3868.jpeg", 'rb')
res = requests.post(url, headers=headers, params=params, files={"image": ("index.jfif", img, "image/jpeg")})
print(res.json())