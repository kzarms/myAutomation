import json

def lambda_handler(event, context):
    #Get phone number from the event.
    phone = event['Details']['ContactData']['CustomerEndpoint']['Address']
    if phone == "+4915222800000":
        resultMap = {"Type":"response","Data":"Hello, Konstantin. This is your personal responce from the lambda function"}
    else:
        resultMap = {"Type":"response","Data":"This is response from the lambda function"}
    return resultMap