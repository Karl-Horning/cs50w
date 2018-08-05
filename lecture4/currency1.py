import requests

# USING FULL RESULTS
def main():
    res = requests.get('https://free.currencyconverterapi.com/api/v6/convert?q=USD_GBP')
    if res.status_code != 200:
        raise Exception('ERROR: API request was unsuccessful.')
    data = res.json()
    rate = data['results']['USD_GBP']['val']
    print(f'1 USD is equal to {rate} GBP')

# USING COMPACT RESULTS
# def main():
#     res = requests.get('https://free.currencyconverterapi.com/api/v6/convert?q=USD_GBP&compact=y')
#     if res.status_code != 200:
#         raise Exception('ERROR: API request was unsuccessful.')
#     data = res.json()
#     rate = data['USD_GBP']['val']
#     print(f'1 USD is equal to {rate} GBP')

if __name__ == '__main__':
    main()