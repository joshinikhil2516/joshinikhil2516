import boto3

vpcResource=boto3.resource("ec2")

groupName="sgsamplebasicusage"
vpcId="vpc-0e40a68d76defca07"

response=vpcResource.create_security_group(
    Description="creating for demo purpose",
    GroupName=groupName,
    VpcId=vpcId,
    TagSpecifications=[{
        "ResourceType":"security-group",
        "Tags":[{'Key':'Name','Value':groupName}]
    }]
    )

print(response.id) #sg-0ca60646ab5727f66