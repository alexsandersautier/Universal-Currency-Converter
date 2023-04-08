import requests, json

def convert(to, fromm, amount):
    url = f"https://api.apilayer.com/fixer/convert?to={to}&from={fromm}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "gkWpJfB8KGgSPqRVHdJWszCB2s71pfa4"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
    result = json.loads(result)

    value = '{:.2f}'.format(result['result'])
    print(f'{amount} {fromm} = {value} {to}')

def what_todo(starting_currency, exchange_currency, value, other='',other2=''):
    if starting_currency == '1' and exchange_currency == '1':
        convert('USD', 'USD', value)
    elif starting_currency == '1' and exchange_currency == '2':
        convert('BRL', 'USD', value)
    elif starting_currency == '2' and exchange_currency == '2':
        convert('BRL', 'BRL', value)
    elif starting_currency == '2' and exchange_currency == '1':
        convert('USD', 'BRL', value)
    elif starting_currency == '3' and exchange_currency == '1':
        convert('USD', other, value)
    elif starting_currency == '3' and exchange_currency == '2':
        convert('BRL', other, value)
    elif starting_currency == '3' and exchange_currency == '3':
        convert(other, other, value)
    elif starting_currency == '1' and exchange_currency == '3':
        convert(other2, 'USD', value)
    elif starting_currency == '2' and exchange_currency == '3':
        convert(other2, 'BRL', value)

while True:
    try:
        other_starting = None
        other_exchange = None
        value = int(input('type any value: '))
        print('Choose any starting  currency')
        print('[1] - USD')
        print('[2] - BRL')
        print('[3] - Other')
        starting_currency = input() 
        if starting_currency == '3':
            other_starting = input('Type currency in three character: ')
        print('[1] - USD')
        print('[2] - BRL')
        print('[3] - Other')
        exchange_currency = input()
        if exchange_currency == '3':
            other_exchange = input('Type currency in three character: ')
        what_todo(starting_currency, exchange_currency, value, other_starting, other_exchange)    
    except ValueError as e:
        print('Only number')    