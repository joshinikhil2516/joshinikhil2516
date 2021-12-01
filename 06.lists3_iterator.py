import boto3

s3=boto3.resource("s3")
iterator=s3.buckets.all()
for b in iterator:
    #print(f"--{b.name}", end=",")
   print(f"--{b.name}")
