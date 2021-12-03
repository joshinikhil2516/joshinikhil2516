import boto3
import logging

class DynamoDBHelper:
    def __init__(self)->None:
        dynamodb=boto3.resource("dynamodb")
        self.table=dynamodb.Table("nikhildbb")

def insertItem(item):
    response=table.put_item(Item=item)
    return(response)

def insertItems(self,items):
    with self.table.batch_writer()as n:
        n.put_item(Items=items[0])
        n.put_item(Items=items[1])
        n.put_item(Items=items[2])
        n.put_item(Items=items[3])
        n.put_item(Items=items[4])
        print(n)
    return()

def getItem(self,k):
    response=self.table.get_item(Key=k)
    return(response)

def getAllScan(self):
    response=self.table.scan()
    return response

def deleteItem(self,d):
    response=self.table.delete_item(Key=d)
    return response

def getName(self,name):
    from boto3.dynamodb.conditions import Key
    response=self.table.query(KeyConditionExpression=Key("Name").eq("Nikhil"))
    return response