import json
import awsgi
from app import app

def lambda_handler(event, context):
    print(json.dumps(event))
    return awsgi.response(app, event, context)