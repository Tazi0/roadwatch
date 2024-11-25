from functools import wraps

def cors_headers(allowed_methods):
    def decorator(func):
        @wraps(func)
        def wrapper(event, context):
            response = func(event, context)
            
            if 'statusCode' not in response:
                return response
            
            if 'headers' not in response:
                response['headers'] = {}
            response['headers'].update({
                "Access-Control-Allow-Methods": f"OPTIONS, {allowed_methods}",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Origin": "*",
            })
            return response
        return wrapper
    return decorator