import boto3


def fnCreateCustomVPC(vpcResource,IpCidr):
    from botocore.exceptions import ClientError
    vpcId="Not Set"
    try:
        response=vpcResource.create_vpc(CidrBlock=IpCidr,
        InstanceTenancy="default",
        TagSpecifications=[{"ResourceType":"vpc","Tags":[{'Key':'Name','Value':'Nikhil1'}]}]
        )
        vpcId=response.id
        print("Created Custom VPC")
    except ClientError as ce:
        print("Not Possible to Create", ce)
    return vpcId
    
#Driver Code Workflow
if __name__=="__main__":
    vpcclient=boto3.resource("ec2",region_name="eu-central-1")
    ip_cidr="192.168.1.0/26" #64
    vpcId=fnCreateCustomVPC(vpcclient,ip_cidr)
    print(vpcId)
