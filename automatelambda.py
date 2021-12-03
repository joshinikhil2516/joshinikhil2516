import boto3
import json
import os
import dynamodbhelper

#01select the IAM role
iam=boto3.client("iam")
role=iam.get_role(RoleName="Nikhil-role-lambda")
print("--------------")
print(role["Role"]["Arn"])
print("-----------------")
#02 zipp the file in lambda
dir_name=r"C:\Python-Training\joshinikhil2516\nikhil"
output_file="handler"
import shutil
shutil.make_archive(output_file,'zip',dir_name)
print("Zip creted")
zippedcode=""
with open("handler.zip","rb") as f:
    zipped_code=f.read()
    print("------zippedcode-----")

#lambdaclient.create_function()
lambdaclient=boto3.client("lambda")
response=lambdaclient.create_function(
    FunctionName="Nikhillambda1",
    Runtime="python3.9",
    Role=role["Role"]["Arn"],
    Handler="handler.lambda_handler",
    Code=dict(ZipFile=zipped_code),
    Timeout=300
)
print(response)