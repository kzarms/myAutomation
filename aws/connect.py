import boto3

client = boto3.client('connect')
myInstance = "2321c696-e1cd-43e4-99b2-1d0baa2e6751"
#Print user list
#Get responce from the API
response = client.list_users(
    InstanceId = myInstance
)
#Print results from the responce
for user in response['UserSummaryList']:
    print(user['Username'])

#
#Get contact flows information
response = client.list_contact_flows(
    InstanceId = myInstance
)
#Print name resutls with type
for item in response['ContactFlowSummaryList']:
    print(item['Name'], item['ContactFlowType'])

#Get phone numbers list per country
response = client.list_phone_numbers(
    InstanceId=myInstance,
    PhoneNumberTypes=['DID']
)
for item in response['PhoneNumberSummaryList']:
    print(item['PhoneNumberCountryCode'], item['PhoneNumber'])

#List of security profiles
response = client.list_security_profiles(
    InstanceId=myInstance,
)
for item in response['SecurityProfileSummaryList']:
    print(item['Id'], item['Name'])

#List of routing profiles
response = client.list_routing_profiles(
    InstanceId=myInstance,
)
for item in response['RoutingProfileSummaryList']:
    print(item['Id'], item['Name'])

#Create user in the connect
response = client.create_user(
    Username='testsdk1106',
    Password='MyP@ssw0rd!',
    IdentityInfo={
        'FirstName': 'Test',
        'LastName': 'UserSDK'
    },
    PhoneConfig={
        'PhoneType': 'SOFT_PHONE',
        'AutoAccept': False,
        'AfterContactWorkTimeLimit': 600
    },
    SecurityProfileIds=[
        '96fb0927-97e1-4a30-a2b7-d874f0ebcfad'
    ],
    RoutingProfileId='306bb995-41c4-436a-bbdb-c4a7658d06d8',
    InstanceId=myInstance,
    Tags={
        'CostCenter': '12345',
        'Env': 'Dev'
    }
)
#Print status code and userID
print(response['ResponseMetadata']['HTTPStatusCode'], response['UserId'])
NewUserId = response['UserId']

#Delete new user
response = client.delete_user(
    InstanceId=myInstance,
    UserId=NewUserId
)
print(response['ResponseMetadata']['HTTPStatusCode'])

print(response)

