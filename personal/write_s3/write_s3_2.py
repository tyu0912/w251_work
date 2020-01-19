import ibm_boto3

key_id = "4066b2f88bd54d4889b0bf82d257fd20"
access_key = "b54905629c37efa543b717866bc97d7f136733bde694d7b6"

session = ibm_boto3.session.Session(aws_access_key_id=key_id, aws_secret_access_key=access_key)
s3 = session.resource("s3")

data = open('test.txt', 'rb')
s3.Bucket('tennisonyu-w251').put_object(Key='text.txt', Body=data)
