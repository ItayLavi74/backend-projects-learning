from flask import Flask, request, jsonify
import secrets
from DB_functions import create_DB_if_not_exists

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    return jsonify("")


if __name__ == '__main__':
    create_DB_if_not_exists()
    app.run(debug=True, host='localhost', port=5000)
