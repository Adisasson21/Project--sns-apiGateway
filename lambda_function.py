import json 
import boto3

def lambda_handler(event, context):
    list1 = event.values()
    sum_calc = sum(list1)
    
    ---  #Added this content to the function for displaying a message in an email 
    notification = f'Here is the SNS notification for Lambda function - the sum calculate is {(lambda x: x)(sum_calc)}'
    client = boto3.client('sns')
    response = client.publish (
      TargetArn = "arn:aws:sns:us-east-1:139091370062:emailme",
      Message = json.dumps({'default': notification}),
      MessageStructure = 'json'
    )
    ---
    return {
      'statusCode': 200,
      'body': json.dumps(response),
      'body': (lambda x: x)(sum_calc)
      
      
    }
