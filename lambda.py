import boto3

client = boto3.client('codebuild')

def start_build(projectname):
    response = client.start_build(
        projectName=projectname,
        environmentVariablesOverride=[
            {
                'name': 'Bucketname',
                'value': 'mybucket987235aaa',
                'type': 'PLAINTEXT'
            }
        ]
        )
    return response    



def lambda_handler(event, context):

    build=(start_build(codebuilddltme_us-east-1_build_Application))
    print(build)