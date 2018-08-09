import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    # Query for the exchange rate
    currency = request.form.get('currency')
    res = requests.get(
        f'https://free.currencyconverterapi.com/api/v6/convert?q=EUR_{currency}')

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({'success': False})

    # Make sure currency is in response
    data = res.json()
    # if currency not in data['results']:
    #     return jsonify({'success': False})

    return jsonify({'success': True, 'rate': data})
