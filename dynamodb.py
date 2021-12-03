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
    "KeyType":"HASH"
},
{
    "AttributeName":"Email",
    "KeyType":"RANGE"
}
]
provisionedThroughput={"ReadCapacityUnits":1,"WriteCapacity":1}

table=dynamodb.create_table(
    TableName="NikhilDDB",
    KeySchema=ks,
    AttributeDefinations=attributeDefinations,
    ProvisionedThroughPut=provisionedThroughput
)

print("Table",table)