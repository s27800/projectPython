from flask import Flask, request, jsonify
from models import (get_all_parking_spots, add_parking_spot,
                    remove_parking_spot, predict_availability,
                    init_db, add_examples,
                    change_parking_spot, check_parameters)

app = Flask(__name__)

@app.route('/api/all_parking_spots', methods=['GET'])
def get_parking_spots():
    parking_spots = get_all_parking_spots()
    return jsonify(parking_spots), 200

@app.route('/api/add_parking_spot', methods=['POST'])
def add_spot():
    json = request.json

    add_parking_spot(
        json['spot_number'],
        json['occupied']
    )

    return jsonify({'status': 'success'}), 201

@app.route('/api/remove_parking_spot/<string:spot_number>', methods=['DELETE'])
def remove_spot(spot_number):
    remove_parking_spot(spot_number)
    return jsonify({'status': 'success'}), 200

@app.route('/api/change_occupied', methods=['PUT'])
def change_occupied():
    json = request.json

    change_parking_spot(
        json['spot_number'],
        json['occupied']
    )

    return jsonify({'status': 'success'}), 200

@app.route('/api/predict_availability', methods=['POST'])
def predict():
    json = request.json

    if not check_parameters(
            json['day_of_week'],
            json['hour'],
            json['is_holiday']
    ):
        return jsonify({'status': 'bad request', 'message': 'Wrong parameters'}), 400

    prediction = predict_availability(
        json['day_of_week'],
        json['hour'],
        json['is_holiday']
    )

    return jsonify({'predicted_number_of_parking_spots': prediction}), 200

@app.route('/init_db')
def initialize_db():
    init_db()
    return jsonify({'status': 'success'}), 200

@app.route('/fill_db')
def fill_db():
    add_examples()
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
