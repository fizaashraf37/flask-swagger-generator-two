from flask import jsonify
from flask import Flask
from flask_swagger_generator.utils import SecurityType
from flask_swagger_generator.swagger_generator import generator, swagger_generator


# Create the flask app
app = Flask(__name__)


request_schema = {
    "id": 10, 
    "name": "level01", 
    "nested_dict": {
        "id":1, 
        "name":"level02",
        "values" : {
            "id": 3,
            "name": "level03"
        }
    }, 
    "nested_list": [
        {"a":1},
        {"b":2}
    ]
}

query_parameters =  [
        {
            "name":"param1",
            "type":"string",
        },
        {
            "name":"param2",
            "type":"int",
        }
    ]

@swagger_generator(
    security_type=SecurityType.BEARER_AUTH,
    tag='Objects',
    request_schema=request_schema,
    response_schema=request_schema,
    query_parameters=query_parameters
)
@app.route('/objects/<int:object_id>', methods=['PUT'])
def get_object(id):
    return jsonify({'id': id, 'name': "test_object"}), 201

generator.generate_swagger(app, destination_path="swagger.yaml")