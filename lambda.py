import boto3

client = boto3.client('codebuild')

def start_build():
    response = client.start_build(
        projectName='codebuilddltme',
        environmentVariablesOverride=[
            {
                'name': 'Bucketname',
                'value': 'mybucket987235aaa',
                'type': 'PLAINTEXT'
            },
            {
                'name': 'destroy',
                'value': 'True',
                'type': 'PLAINTEXT'
            }
        ],
        idempotencyToken='string01'
        )
    print(response)    
    return response    



def lambda_handler(event, context):
    
    start_build()
    #build = (start_build(codebuilddltme_us-east-1_build_Application))
    #print(build)