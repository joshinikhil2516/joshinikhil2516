import boto3
import pathlib

BASE_DIR=pathlib.Path(__file__).parent.resolve()
bucket_name="nishibucket9333"
#file_name=f"{BASE_DIR}\requirements.txt"
file_name="C:\Python-Training\joshinikhil2516\requirements.txt"
object_name="requirements.txt"
s3client=boto3.client("s3")
print("File Uploaded")
print (file_name)
#print(BASE_DIR+"\\"+file_name)

#s3client.upload_file(BASE_DIR+ "\\"+file_name,bucket_name,object_name)