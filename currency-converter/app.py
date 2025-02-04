from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    api_key = 'YOUR_API_KEY'
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    converted_amount = rate * amount

    return render_template('result.html', from_currency=from_currency, to_currency=to_currency,
                           amount=amount, converted_amount=converted_amount)

if __name__ == '__main__':
    app.run(debug=True)