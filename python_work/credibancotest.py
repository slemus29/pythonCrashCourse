import json
import sys

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

event = {'version': '2.0', 'routeKey': 'POST /crear-orden', 'rawPath': '/crear-orden', 'rawQueryString': '', 'headers': {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'cache-control': 'no-cache', 'content-length': '87', 'content-type': 'application/json', 'host': '89b7x0bg09.execute-api.us-east-2.amazonaws.com', 'postman-token': 'd211c32d-a7c2-47e6-ba33-694173c542e0', 'user-agent': 'PostmanRuntime/7.42.0', 'x-amzn-trace-id': 'Root=1-670c497e-5ae6077a2dea160d52fd6438', 'x-forwarded-for': '54.86.50.139', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'requestContext': {'accountId': '461041554713', 'apiId': '89b7x0bg09', 'domainName': '89b7x0bg09.execute-api.us-east-2.amazonaws.com', 'domainPrefix': '89b7x0bg09', 'http': {'method': 'POST', 'path': '/crear-orden', 'protocol': 'HTTP/1.1', 'sourceIp': '54.86.50.139', 'userAgent': 'PostmanRuntime/7.42.0'}, 'requestId': 'fnBrxiD0iYcEPwQ=', 'routeKey': 'POST /crear-orden', 'stage': '$default', 'time': '13/Oct/2024:22:28:14 +0000', 'timeEpoch': 1728858494224}, 'body': '{\n    "id": 1,\n    "product": "galletas",\n    "status": "pending" ,\n    "quantity":10\n}', 'isBase64Encoded': False}

get_file_content = event["body"]
x = json.loads(get_file_content)

print(x)