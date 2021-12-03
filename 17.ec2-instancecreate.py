import boto3

ec2=boto3.resource("ec2")
keyPairName="nikhilkp1"
imageid="ami-0ed9277fb7eb570c9"

instances=ec2.create_instances(
    MinCount=1,
    MaxCount=2,
    ImageId=imageid,
    InstanceType="t2.micro",
    KeyName=keyPairName,
    TagSpecifications=[{
        "ResourceType":"instance",
        "Tags":[{
            "Key":"Name",
            "Value":"Nikhilinstance"
        }]
    }]
)

for instance in instances:
    print("Instance is Created with the following id as:", instance.id)

    instance.wait_until_running()
    print("Instance is started")