import boto3
import json

rds=boto3.client("rds")

response=rds.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    DBInstanceIdentifier="Nikhildb1",
    Engine="MySQL",
    MasterUserPassword="testpwd0021",
    MasterUsername="admin01"
)
print(json.dumps(response,indent=4))