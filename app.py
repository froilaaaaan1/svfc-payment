from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@host:port/database_name'
db = SQLAlchemy(app)

@app.route('/pay', methods=['POST'])
def pay():
    data = request.get_json()
    print(data)
    return jsonify({'status': 'success'})