from flask import Blueprint, jsonify, request
from marshmallow_generic import GenericSchema, fields

# NOTE: We can use marshmallow to validate the request
# NOTE: This requires `poetry add typing-extensions marshmallow-generic`

twosum_rest_v1 = Blueprint('twosum_rest',
                           __name__,
                           url_prefix='/api/v1/twosum')


class TwoSum:
    def __init__(self, target, values):
        self.target = target
        self.values = values


class TwoSumSchema(GenericSchema[TwoSum]):
    target = fields.Integer(required=True)
    values = fields.List(fields.Integer(), required=True)


@twosum_rest_v1.route('/')
def two_sum():
    # NOTE: We can unpack the json of the request here
    data = request.get_json()
    # NOTE: If we wanted to we could use `loads` and load the JSON directly
    result = TwoSumSchema().load(data)
    print('types', type(result))
    print('nice', result.target)
    num_map = {}
    for i, num in enumerate(result.values):
        complement = result.target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return jsonify({'message': 'No solution found'})
