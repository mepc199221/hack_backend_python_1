from flask import Flask, jsonify, request
from flask_cors import CORS





app = Flask(__name__)
CORS(app)

#HACK1
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'payload': 'success'})

#HACK2
@app.route('/user', methods=['POST'])
def post_user():
    return jsonify({'payload': 'success'})

#HACK3
@app.route('/user', methods=['DELETE'])
def delete_user():
    return jsonify({'payload': 'success'})

if __name__ == "__main__":
    app.run(debug=True)

#HACK4
@app.route('/user', methods=['PUT'])
def put_user():
    return jsonify({'payload': 'success',
    "error": False})

#HACK5
@app.route('/api/v1/users', methods=['GET'])
def api_get_users():
    return jsonify({
        "payload":[]})

#HACK6 
@app.route('/api/v1/user', methods=['POST'])
def post_api_user():
    email = request.args.get('email')
    name = request.args.get('name')
    response = {
        'payload': {
            'email': email,
            'name': name
        }
    }
    
    return jsonify(response)


#HACK7
@app.route('/api/v1/user/add', methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': user_id
        }
    })

#HACK8 
@app.route('/api/v1/user/create', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    user_id = data.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': user_id
        }
    })




if __name__ == "__main__":
    app.run(debug=True)