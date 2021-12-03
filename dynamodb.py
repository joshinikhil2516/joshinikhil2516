import boto3
import json
import os
import logging

dynamodb=boto3.resource("dynamodb")
ks=[
    {
    "AttributeName":"Name",
    "KeyType":"HASH"
},
{
    "AttributeName":"Email",
    "KeyType":"RANGE"
}
]
attributeDefinations=[
    {
    "AttributeName":"Name",
    "AttributeType":"S"
},
{
    "AttributeName":"Email",
    "AttributeType":"S"
}
]
provisionedThroughput={"ReadCapacityUnits":1,"WriteCapacityUnits":1}

table=dynamodb.create_table(
    TableName="nikhildbb",
    KeySchema=ks,
    AttributeDefinitions=attributeDefinations,
    ProvisionedThroughput=provisionedThroughput
)

print("Table",table)