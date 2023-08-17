from flask import Blueprint, request, jsonify

from .linkedlist import deleteNode, insertNode, makeList, addNode, getNode

ll_rest_v1 = Blueprint('ll_rest', __name__, url_prefix='/api/v1/linkedlist')


@ll_rest_v1.route('/<position>')
def get_node(position: int):
    return str(getNode(int(position)))


@ll_rest_v1.route('/add', methods=['POST'])
def add_node():
    request_data = request.get_json()
    print(request_data)
    addNode(request_data['nice'])
    return makeList()


@ll_rest_v1.route('/delete/<node>', methods=['DELETE'])
def delete_node(node: str):
    deleteNode(node)
    return jsonify({'message': 'deleted'})


@ll_rest_v1.route('/insert/<position>', methods=['PUT'])
def next_node(position: str):
    request_data = request.get_json()
    insertNode(request_data['nice'], int(position))
    return jsonify({'message': 'inserted'})
