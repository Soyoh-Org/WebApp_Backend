from flask import request, Flask, jsonify
from pathlib import Path
from dbclient import queries
import logging

app = Flask(__name__)
app.config['DEBUG'] = True

Path('C:/WebApi/Logs').mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename='C:/WebApi/Logs/api.log', level=logging.DEBUG)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Web API</h1><p>This site is a prototype API.</p>'


@app.route('/users', methods=['GET'])
def users():
    try:
        result = queries.find('employees')
        return jsonify(result), 200
    except (IndexError, TypeError) as e:
        return {'error': str(e)}, 500


@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def mock_user_requests():
    if request.method == 'GET':
        try:
            result = queries.find('employees', request.args)
            return jsonify(result), 200
        except (IndexError, TypeError) as e:
            return {'error': str(e)}, 500

    if request.method == 'POST':
        try:
            result = queries.insert('employees', request.json)
            return jsonify(result), 201
        except (IndexError, TypeError) as e:
            return {'error': str(e)}, 500

    if request.method == 'DELETE':
        try:
            result = queries.delete('employees', request.args)
            return jsonify(result), 200
        except (IndexError, TypeError) as e:
            return {'error': str(e)}, 500


app.run(host='0.0.0.0')
