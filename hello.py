from urllib import response
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/products')
def products():
    response = jsonify([
        {
            "title": "Caneca personalizada de Porcelana Backend",
            "amount": 123.45,
            "installments": {"number": 3, "total": 41.45, "hasFee": True},
        },
        {
            "title": "Caneca de Tulipa",
            "amount": 123.45,
            "installments": {"number": 3, "total": 41.45},
        }
    ])

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
