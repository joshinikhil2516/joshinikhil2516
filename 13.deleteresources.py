import boto3
import logging

logger=logging.getLogger()
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

vpcClient=boto3.client("ec2") #vpc ids details: vpc-0f30a610f369d8264--us-east-1,vpc-092316deb7c3b551d--eu-central-1
#vpcClient1=boto3.client("ec2",region_name="us-east-1") #vpc ids details: vpc-0f30a610f369d8264--us-east-1,vpc-092316deb7c3b551d--eu-central-1


def fnVPCDelete(vpcId):
    from botocore.exceptions import ClientError 
    vpc=None    
    try:
        vpc=vpcClient.delete_vpc(VpcId=vpcId)
        logger.info("Listing VPC done")       
    except ClientError as ce:
        print("Found Error :", ce)
        logger.exception("Not Possible........")
    return vpc
    
#Driver Code Workflow
if __name__=="__main__":
    vpcLists=fnVPCDelete(vpcId="vpc-0f30a610f369d8264")
    print("deleted")
