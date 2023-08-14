from flask import Blueprint, request, jsonify

from poetry_demo.linkedlists.linkedlist import deleteNode, insertNode

from poetry_demo.linkedlists.linkedlist import makeList, addNode, getNode


ll_rest = Blueprint('ll_rest', __name__, url_prefix='/api/v1/llist')


@ll_rest.route('/<position>')
def get_node(position: int):
    return str(getNode(int(position)))


@ll_rest.route('/add', methods=['POST'])
def add_node():
    request_data = request.get_json()
    print(request_data)
    addNode(request_data['nice'])
    return makeList()


@ll_rest.route('/delete/<node>', methods=['DELETE'])
def delete_node(node: str):
    deleteNode(node)
    return jsonify({'message': 'deleted'})


@ll_rest.route('/insert/<position>', methods=['PUT'])
def next_node(position: str):
    request_data = request.get_json()
    insertNode(request_data['nice'], int(position))
    return jsonify({'message': 'inserted'})
