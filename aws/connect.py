import boto3

#Test connection with boto3
#iam = boto3.client('iam')
#paginator = iam.get_paginator('list_users')
#for response in paginator.paginate():
#    print(response)

client = boto3.client('connect')


response = client.list_phone_numbers()
print(response)

response = client.list_users(
    InstanceId='2321c696e1cd43e499b21d0baa2e6751'
)
print(response)
"""


client = boto3.client('chime')

client.c

AccountName = "CallCenter3105"
#Create main account
response = client.create_account(
    Name='CallCenter3105'
)
print(response)
AccountID = response["Account"]["AwsAccountId"]


response = client.associate_phone_number_with_user(
    AccountId=AccountID,
    UserId='string',
    E164PhoneNumber='string'
)

#Create Users

response = client.create_user(
    AccountId=AccountID,
    Username='user1',
    Email='me@ikot.eu',
    UserType='PrivateUser'
)


response = client.invite_users(
    AccountId=AccountID,
    UserEmailList=[
        'ikotpad@gmail.com',
    ],
    UserType='PrivateUser'
)

response = client.get_user(
    AccountId=AccountID,
    UserId='string'
)

print(response)
"""