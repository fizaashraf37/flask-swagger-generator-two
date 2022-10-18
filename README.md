# Flask Swagger Generator Two
Flask swagger generator is a library to create Swagger Open API definitions 
for Flask based applications. Swagger is an Interface Description Language for describing REST 
APIs expressed using JSON and YAML. 

This library is an enhancement of [flask-swagger-generator](https://github.com/coding-kitties/flask-swagger-generator) library which was originally developed by [coding-kitties](https://github.com/coding-kitties)

## Installing 
This library is not available on pip since this is an enhancement. You can clone its code from git and import it as a package in your project. Once the original library is published with latest version including all fixes and features that I have added in this library then you can directly install this from pip.

## Documentation
COMING SOON

## A Simple Example

```python
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
```


## Features Added

- Support for adding server URL
- Support for nested schemas in request/response (nested schema for Marshmallow schema type will be added soon)
- Support for input type `path` parameter 
- Support for `Query Parameters`
- Support for adding URL base
- Support for marshmallow `Function` and `Mapping` feild types 
- Support for grouping endpoints by prodiving custom tags

## Fixes

- Generator.generate_swagger was not working if destination path is not provided
