# The previous API has been restricted, so free.currencyconverterapi is used instead
import requests

# FULL RESULTS
def main():
    res = requests.get('https://free.currencyconverterapi.com/api/v6/convert?q=USD_GBP')
    if res.status_code != 200:
        raise Exception('ERROR: API request was unsuccessful.')
    data = res.json()
    print(data)

# COMPACT RESULTS
# def main():
#     res = requests.get('https://free.currencyconverterapi.com/api/v6/convert?q=USD_GBP&compact=y')
#     if res.status_code != 200:
#         raise Exception('ERROR: API request was unsuccessful.')
#     data = res.json()
#     print(data)

if __name__ == '__main__':
    main()