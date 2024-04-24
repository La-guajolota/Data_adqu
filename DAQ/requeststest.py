import requests

data = {"temp":12.32}

response = requests.post("http://172.20.10.9/savedata.php",json=data)
print("Status code: ", response.status_code)
print("json response: ", response.json())