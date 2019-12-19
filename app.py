from flask import Flask, request, jsonify, json, send_from_directory
from flask_cors import CORS
import requests
from datetime import datetime, timedelta

app = Flask(__name__, static_url_path='')
CORS(app)

OK_STATUS_CODE = 200
BAD_REQUEST_STATUS_CODE = 400

API_KEY = '57UUZTV62RHDUH41'
URL_START = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
URL_END = '&apikey=' + API_KEY

def generate_response(response, status, headers={}):
    response.status_code = status
    response.headers = {**{
        'Content-Type': 'application/json'
    }, **headers}
    return response


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/guess/<symbol_str>/<guess_str>', methods=["GET"])
def guess(symbol_str, guess_str):
    try:
        yesterday_str = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        resp = requests.get(url = URL_START + symbol_str + URL_END).json()
        res = int(float(resp['Time Series (Daily)'][yesterday_str]["4. close"]))
        guess_int = int(guess_str)
        msg = 'correct!'
        if guess_int < res:
            msg = 'too low!'
        elif guess_int > res:
            msg = 'too high!'
        return generate_response(jsonify({
            'success': True,
            'message': msg
        }), OK_STATUS_CODE)
    except:
        return generate_response(jsonify({
            'success': False,
            'message': 'not processable.. Sorry!'
        }), BAD_REQUEST_STATUS_CODE)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)