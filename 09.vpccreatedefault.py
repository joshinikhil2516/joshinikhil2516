import boto3

from botocore.exceptions import ClientError

vpcclient=boto3.client("ec2")

vpcId=""
try:
    response=vpcclient.create_default_vpc()
    vpcId=response["Vpc"]["VpcId"]
    print("Created Default VPC")
except ClientError:
    print("Not Possible to Create")
print (vpcId)