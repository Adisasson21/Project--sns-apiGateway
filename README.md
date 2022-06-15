# Project--sns-apiGateway

Under the test tab: 
  {
  "number1": 2,
  "number2": 5
}

# Search for IAM:
  first we need to create a IAM  --> Roles --> choose AWS Service --> Use case: lambda  && ApiGateway --> next --> Under the Permissions policies find this 3 /
  1.AmazonSNSFullAccess
  2.AmazonSNSRole
  3.AWSLambdaExecute
  --> next --> create role. 
  

# create sns:
--> goto Amazom sns
-->create topic for 
-->create sub to the email and confirm from the email 
-->create a IAM role for the delivery status logging



# Set up the ApiGateway:
--> Goto apiGateway
-->create API --> HTTP API --> BUILD
-->For Integrations --> Add integration --> Choose Lambda --> choose the ARN's lambda --> named API NAME
-->under Configure routes --> choose GET + POST Methods

# Come back to your lambda function.
Under the configuration tab : 
--> goto triggers and set ApiGateway && SNS
-->goto permissions: --> edit Execution role --> at the bottom set your Existing role that we made earler. 
