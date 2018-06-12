import json

from flask import Flask, Response
from flask import request
from gevent.pywsgi import WSGIServer

from db.models import Bundle, session

app = Flask(__name__) # Initialize flask app

HEADERS = {'Content-Type': 'application/json'} # set default headers for requests


def is_valid_input(payload):
    # Validates the input that are passed for creation of the bundle
    try:
        if payload['sensor_type'] not in ['humidity', 'temperature']:
            return False
        if not isinstance(payload['device_uuid'], str):
            return False
        if not isinstance(payload['sensor_value'], float) or payload['sensor_value'] > 100 or payload['sensor_value'] < 0:  #input range for sensor lookup 
            return False
        if not isinstance(payload['sensor_reading_time'], int):
            return False
        return True
    except KeyError:
        return False


def generate_query(query_params):
    # convert the url query string into the database query
    query = session.query(Bundle)
    if query_params.get('sensor_type'):
        if query_params['sensor_type'] not in ['humidity', 'temperature']:
            return False
        query = query.filter(Bundle.sensor_type == query_params['sensor_type'])
    if query_params.get('device_uuid'):
        if not isinstance(query_params['device_uuid'], str):
            return False
        query = query.filter(Bundle.device_uuid == query_params['device_uuid'])
    if query_params.get('start_time'):
        try:
            start_time = int(query_params['start_time'])
            query = query.filter(Bundle.sensor_reading_time >= start_time)
        except ValueError:
            return None
    if query_params.get('end_time'):
        try:
            end_time = int(query_params['end_time'])
            query = query.filter(Bundle.sensor_reading_time <= end_time)
        except ValueError:
            return None
    return query


@app.route('/bundles', methods=['GET', 'POST'])
def bundles():
    if request.method == 'GET':
        # handles the GET request
        all_args = request.args.to_dict()
        query = generate_query(all_args)
        if not query:
            return Response(json.dumps({'error': 'Invalid Search params: Inputs: Sensor_type: Humidity or Temperature, Sensor Value should be between 0 and 100 inclusive, device UUID is a string, device start and end times are integers '}), status=400, headers=HEADERS)
        data = [r.to_dict() for r in query]
        return Response(json.dumps(data), status=200, headers=HEADERS)

    if request.method == 'POST':
        # handles the POST request for creating the bundle
        data = request.json
        if not is_valid_input(data):
            return Response(json.dumps({'error': 'Invalid Post params, Please make sure Inputs are: Sensor_type: Humidity or Temperature, Sensor Value should be between 0 and 100 inclusive inputted as a float, device UUID is a string, sensor_reading_time is an integer '}), status=400, headers=HEADERS)
        bundle = Bundle(**data)
        session.add(bundle)
        session.commit()
        return Response(json.dumps(bundle.to_dict()), status=201, headers=HEADERS)


if __name__ == '__main__':
    # start the server
    WSGIServer(('127.0.0.1', 5000), app).serve_forever()
    # app.run(debug=True)
