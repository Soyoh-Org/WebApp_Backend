from flask import request, Flask, jsonify
from pathlib import Path
from bson import json_util
from dbclient import Session
from collections import namedtuple
import logging
import json

app = Flask(__name__)
app.config['DEBUG'] = True
Path('C:/WebApi/Logs').mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename='C:/WebApi/Logs/api.log', level=logging.DEBUG)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Web API</h1><p>This site is a prototype API.</p>'


@app.route('/users', methods=['GET'])
def users():
    employee_collection = Session.employees
    employees = []
    for item in employee_collection.find():
        employees.append(json.loads(json.dumps(item, indent=4, default=json_util.default)))

    return jsonify(employees)


@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def mock_user_requests():
    if request.method == 'GET':
        if 'id' in request.args and request.args['id']:
            user_id = request.args['id']
        else:
            return '<p>Error: No id field provided. Please specify an id.</p>', 404

        json_data = read_json_file()

        for x in json_data['users']:
            if x['id'] == user_id:
                return jsonify(x)

        return '<p>There was a problem the request.</p>', 404

    if request.method == 'POST':
        data = request.json
        write_json_file(data)
        return '<p>The user was successfully added.</p>', 201

    if request.method == 'DELETE':
        if 'id' in request.args and request.args['id']:
            user_id = request.args['id']
        else:
            return '<p>Error: No id field provided. Please specify an id.</p>', 404

        json_data = read_json_file()

        for element in json_data['users']:
            if user_id == element['id']:
                json_data['users'].remove(element)

        with open('mockdata/mock.json', 'w') as outfile:
            json.dump(json_data, outfile, indent=4, sort_keys=True)
        return '<p>The user with the id: {} was successfully deleted.</p>'.format(user_id), 200


def read_json_file():
    with open('mockdata/mock.json') as json_file:
        return json.load(json_file)


def write_json_file(data):
    json_data = read_json_file()
    json_data['users'].append(data)

    with open('mockdata/mock.json', 'w') as outfile:
        json.dump(json_data, outfile, indent=4, sort_keys=True)


app.run(host='0.0.0.0')
