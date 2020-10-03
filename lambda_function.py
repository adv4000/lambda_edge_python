#--------------------------------------------------------------
# Lambda@Edge Function to Ask Password for access to CLoudFront
# Python 3.8
# Lambda@Edge to be created in US-EAST-1 ONLY!
# Developed by Denis Astahov 02-October-2020
#--------------------------------------------------------------
import base64

USERNAME = "admin"
PASSWORD = "adminadmin"

def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    headers = request['headers']

    auth_user_password = (USERNAME + ':' + PASSWORD).encode('ascii')
    auth_token = base64.b64encode(auth_user_password).decode()
    auth_string = 'Basic ' + auth_token
    if 'authorization' not in headers or headers['authorization'][0]['value'] != auth_string:
        return {
                "status": '401',
                "statusDescription": 'Unauthorized',
                "body"             : 'Unauthorized',
                "headers": {
                    'www-authenticate': [
                    {"key": 'WWW-Authenticate', "value":'Basic'}
                 ]}  
                }
    return request  
