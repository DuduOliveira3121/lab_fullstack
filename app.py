from flask import Flask, request, jsonify
from service.user_service import UserService
from model.user import validate_user_data

app = Flask(__name__)

# instância do service (usa o model internamente)
service = UserService()


@app.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    ok, err = validate_user_data(data)
    if not ok:
        return jsonify({"error": err}), 400

    user = service.create_user(data)
    if user is None:
        return jsonify({"error": "CPF já cadastrado"}), 400

    return jsonify(user), 201


@app.route('/users', methods=['GET'])
def list_users_route():
    return jsonify(service.list_users()), 200


@app.route('/users/<cpf>', methods=['GET'])
def get_user_route(cpf):
    user = service.get_user_by_cpf(cpf)
    if user is None:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user), 200


@app.route('/users/<cpf>', methods=['DELETE'])
def delete_user_route(cpf):
    deleted = service.delete_user(cpf)
    if deleted:
        return ('', 204)
    return jsonify({"error": "Usuário não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)