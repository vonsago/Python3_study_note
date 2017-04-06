import  requests

stockList=[]

res = requests.get('https://api.github.com/user', auth=('user', 'pass'))

data = str(res.content)

stockList = data.split(',')

print(stockList)

print("res.status_code:")

print(res.status_code)

print("res.headers['content-type']:"+res.headers['content-type'])

print("res.encoding:"+res.encoding)

print("res.text"+res.text)

print("res.json():")


print(res.json())

