import requests
x=2
y=3
operation="add"
response=requests.post(url=f"http://localhost:8000/{operation}",json={"x":x , "y":y})

if response.status_code==200 :
    d=response.json()
    value=d['result']
    print (value)
else :
    print(response.text)
