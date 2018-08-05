import requests

def main():
    base = input('First Currency: ')
    other = input('Second Currency: ')
    res = requests.get(f'https://free.currencyconverterapi.com/api/v6/convert?q={base}_{other}')
    if res.status_code != 200:
        raise Exception('ERROR: API request was unsuccessful.')
    data = res.json()
    rate = data['results'][f'{base}_{other}']['val']
    print(f'1 {base} is equal to {rate} {other}')

if __name__ == '__main__':
    main()