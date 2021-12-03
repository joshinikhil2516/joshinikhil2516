import boto3
import json

#ec2=boto3.resource("ec2")

#key_pair=ec2.KeyPair("nikhilkp")

#print(key_pair)

ec2=boto3.client("ec2")
mykeyname="nikhilkp1"
response=ec2.create_key_pair(KeyName=mykeyname)
with open(mykeyname+".pem","w") as f:
    f.write(response["KeyMaterial"])
#f=OpenBinaryMode(mykeyname+".pem","w")
#f.write(response["KeyMaterial"])
#f.close()
print(response)
