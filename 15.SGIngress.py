import boto3
import json

vpcClient=boto3.client("ec2")
sgId="sg-0ca60646ab5727f66"
IPP1={
    "IpProtocol":"tcp",
    "FromPort":80,
    "ToPort":80,
    "IpRanges":[{"CidrIp":"0.0.0.0/0"}]
    }
IPP2={
    "IpProtocol":"tcp",
    "FromPort":22,
    "ToPort":22,
    "IpRanges":[{"CidrIp":"0.0.0.0/0"}]
    }
response=vpcClient.authorize_security_group_ingress(GroupId=sgId,
IpPermissions=[IPP1,IPP2])

print(json.dumps(response,indent=4))
