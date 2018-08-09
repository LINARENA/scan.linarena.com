import requests

r = requests.post("https://api.eosnewyork.io/v1/history/get_actions",
                  json = {'pos': -1,
                          "offset": -20,
                          "account_name": "geydmnrzgene"})

for data in r.json()['actions']:
    print(data)
