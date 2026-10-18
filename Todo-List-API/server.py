from flask import Flask, request, jsonify
import secrets
from DB_functions import create_DB_if_not_exists, add_user
from validation import validate_register
import json
from dataclasses import dataclass

app = Flask(__name__)


@dataclass
class Response:
    massage: str | None = None
    description: str | list = ""


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    validation_response = validate_register(data)

    if not validation_response.ok:
        return jsonify(Response(massage="Failed registration", description=validation_response.errors)), 400

    add_user(data, '1')

    return jsonify(Response(massage='Successful registration', description='Your account has been created successfully')), 201


if __name__ == '__main__':
    create_DB_if_not_exists()
    app.run(debug=True, host='localhost', port=5000)
