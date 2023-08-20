from flask import Flask, render_template, request, jsonify
from data_fetching import fetch_data
from data_preprocessing import preprocess_data

app = Flask(__name__)

@app.route('/fetch_data', methods=['POST'])
def fetch_data_route():
    symbol = request.json['symbol']
    currency = request.json['currency']
    data = fetch_data(symbol, "DIGITAL_CURRENCY_DAILY", currency)
    if data is None:
        return jsonify({'error': 'Error fetching data.'}), 500
    preprocessed_data = preprocess_data(data)
    return preprocessed_data.to_json()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
