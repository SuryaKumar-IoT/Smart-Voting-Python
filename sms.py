import boto3

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="Replace with your ID",
    aws_secret_access_key="Replace with your Secret key",
    region_name="us-east-1"
)

def sendsms(a,b):
    #print(a,b)
    client.publish(
        PhoneNumber=a,
        Message=b
    )
    print("message sent")

#sendsms('+917799204041','Good Evening')
