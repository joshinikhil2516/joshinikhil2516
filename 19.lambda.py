import boto3
import json
import os

iam=boto3.client("iam")
role=iam.get_role(RoleName="Nikhil-role-lambda")
print("--------------")
print(role["Role"]["Arn"])
print("-----------------")
lambdaclient=boto3.client("lambda")
zippedcode=""
with open("handler.zip","rb") as f:
    zipped_code=f.read()
    print("------zippedcode-----")

#lambdaclient.create_function()
response=lambdaclient.create_function(
    FunctionName="Nikhillambda",
    Runtime="python3.9",
    Role=role["Role"]["Arn"],
    Handler="handler.lambda_handler",
    Code=dict(ZipFile=zipped_code),
    Timeout=300
)
print(response)