import boto3
vpcClient=boto3.client("ec2",region_name="eu-central-1") #vpc ids details: vpc-0f30a610f369d8264--us-east-1,vpc-092316deb7c3b551d--eu-central-1
vpcClient1=boto3.client("ec2",region_name="us-east-1") #vpc ids details: vpc-0f30a610f369d8264--us-east-1,vpc-092316deb7c3b551d--eu-central-1


def fnVPCDescribe(tagKey,tagValues,maxitems):
    from botocore.exceptions import ClientError
    vpcLists=[]    
    try:
        paginator=vpcClient.get_paginator("describe_vpcs")
        paginator=vpcClient1.get_paginator("describe_vpcs")
        response_iterator=paginator.paginate(Filters=[
            {
                'Name':f'tag:{tagKey}',
                 'Values':tagValues
                
            }
            ],PaginationConfig={'MaxItems':maxitems})
        full_result=response_iterator.build_full_result()
        for page in full_result["Vpcs"]:
                vpcLists.append(page)
        print("list the created vpc")
    except ClientError as ce:
        print("Not Possible to Create", ce)
    return vpcLists
    
#Driver Code Workflow
if __name__=="__main__":
    vpcLists=fnVPCDescribe(tagKey="Name",tagValues=["Nikhil","Nikhil1","vpc64mujahed"],maxitems=10)
    
    import json
    for vpc in vpcLists:
        print(json.dumps(vpc,indent=4))
