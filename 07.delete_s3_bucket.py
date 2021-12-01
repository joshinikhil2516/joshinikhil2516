import boto3
##s3resource=boto3.resource("s3")
#Bucket=s3resource.Bucket("bkt038nikhil")
#Bucket.delete()

##s3client=boto3.client("s3")
##s3client.delete_bucket(Bucket="bkt038nikhil")
#print("Bucket Deleted")

s3resource=boto3.resource("s3")
bucketName="nikhil-delete-bucket"
Bucket=s3resource.Bucket(bucketName)

def cleanup_bucket_objects(myBucket):
    for obj in myBucket.objects.all():
        obj.delete()
    for objVer in myBucket.object_versions.all():
        objVer.delete()

cleanup_bucket_objects(Bucket)
Bucket.delete()   

print("objects deleted")