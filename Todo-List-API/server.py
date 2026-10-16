from flask import Flask, request, jsonify
import secrets
from DB_functions import create_DB_if_not_exists
from validation import validate_register
import json

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    validation_response = validate_register(data)

    return jsonify(validation_response)


if __name__ == '__main__':
    create_DB_if_not_exists()
    app.run(debug=True, host='localhost', port=5000)
