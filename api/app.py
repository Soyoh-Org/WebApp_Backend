from flask import request, Flask, jsonify
import logging
import json
from pathlib import Path

app = Flask(__name__)
app.config['DEBUG'] = True
Path('C:/WebApi/Logs').mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename='C:/WebApi/Logs/api.log', level=logging.DEBUG)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Web API</h1><p>This site is a prototype API.</p>'


@app.route('/users', methods=['GET'])
def users():
    users_data = read_json()
    return users_data


@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def user_by_id():
    if request.method == 'GET':
        json_data = read_json()

        if 'id' in request.args and request.args['id']:
            user_id = request.args['id']
        else:
            return 'Error: No id field provided. Please specify an id.', 404

        for x in json_data['users']:
            if x['id'] == user_id:
                return jsonify(x)
        return '<p>There was a problem the request.</p>', 404


def read_json():
    with open('mockdata/mock.json') as json_file:
        return json.load(json_file)


app.run(host='0.0.0.0')
