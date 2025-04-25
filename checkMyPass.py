import requests

url = 'https://api.pwnedpasswords.com/range/' + '123456789' #nga ktu kuptojme sa i lehte eshte pass ne baze te response tek cmd
res = requests.get(url)   # ne vend te pass mund te vendosim vetem 5 shifrat e para te HASH GEN te pass qe e marrim tek
print(res)                 # website https://passwordsgenerator.net/sha1-hash-generator/

