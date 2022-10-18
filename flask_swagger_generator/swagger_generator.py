import functools
from flask_swagger_generator.generators import Generator
from flask_swagger_generator.specifiers import SwaggerVersion

generator = Generator.of(SwaggerVersion.VERSION_THREE)


def conditional(decorator, condition):
    def resdec(func):
        if condition:
            return decorator(func)
        else:
            return func

    return resdec


def swagger_generator(
    security_type=None,
    tag=None,
    request_schema=None,
    response_schema=None,
    status_code=200,
    response_description='',
    query_parameters=None
):
    def accumulate_wrapper(func):
        @conditional(generator.security(security_type), security_type is not None)
        @conditional(generator.path_tag(tag), tag is not None)
        @conditional(generator.request_body(request_schema), request_schema is not None)
        @conditional(generator.query_parameters(query_parameters), query_parameters is not None)
        @conditional(generator.response(
                            status_code=status_code, 
                            schema=response_schema, 
                            description=response_description
                            ), 
                            response_schema is not None)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return accumulate_wrapper
