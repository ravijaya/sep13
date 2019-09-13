from flask import Flask, jsonify, request, abort
from usermodel import select_all_users, select_user_by_id, add_user_model
import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='access.log')


app = Flask(__name__)


@app.route('/users', methods=['POST'])
def user_add():
    logging.debug(f"recv : {request.json}")

    if not ('name' in request.json and 'ugroup' in request.json and 'email' in request.json):
        abort(400)

    values = request.json.get('name'), request.json.get('ugroup'), request.json.get('email')
    user = add_user_model(values)
    return jsonify(dict(user=user)), 201


@app.route('/users', methods=['GET'])
def get_list_of_users():
    payload = {'users': select_all_users()}
    return jsonify(payload)


@app.route('/users/<int:uid>', methods=['GET'])
def get_user_by_id(uid):
    user = select_user_by_id(uid)
    return jsonify({'user': user})


if __name__ == '__main__':
    app.run(debug=True)
