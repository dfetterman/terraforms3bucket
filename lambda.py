import boto3
import json
from datetime import date, datetime

client = boto3.client('codebuild')
s3 = boto3.resource('s3')


def response(message, status_code):
    return {
        'statusCode': str(status_code),
        #'body': json.dumps(message),
        'body': message,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true'
            },
        }


def start_build():
    response = client.start_build(
        projectName='codebuilddltme',
        environmentVariablesOverride=[
            {
                'name': 'Bucketname',
                'value': 'mybucket987235aaa1',
                'type': 'PLAINTEXT'
            },
            {
                'name': 'destroy',
                'value': 'True',
                'type': 'PLAINTEXT'
            }
        ],
        idempotencyToken='string0a1d'
        )
    print(json.dumps(response['build']['buildStatus']).strip('"'))
    return(json.dumps(response['build']['buildStatus']).strip('"'))  


def get_artifacts():
    content_object = s3.Object('codebuilddltme1.us-east-1.terraform-state-software', 'codebuilddltme/artifacts.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    try:
        BucketnameOutput=json_content['BucketnameOutput']['value']
    except KeyError:
        print("We were unable to pull the value from the artifacts")
        BucketnameOutput = "NULL"
    try:
        SG=json_content['SG1']['value']    
    except KeyError:
        print("We were unable to pull the value from the artifacts")
        SG = "NULL"

    print(BucketnameOutput)
    print(SG)
    return(json_content)


def lambda_handler(event, context):
    
    #start_build()
    artifacts = ""
    build = start_build()
    
    if build == "SUCCEEDED":
        print("Build succeeded, getting artifacts")
        artifacts = get_artifacts()
        statusCode = "200"
    elif build == "IN_PROGRESS":
        statusCode = "200"
    elif build == "FAILED":
        statusCode = "500"
    else:
        statusCode = "200"

    return response({'status': build, 'artificats': artifacts }, statusCode)
