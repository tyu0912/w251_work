import ibm_boto3
from ibm_botocore.client import Config

api_key = 'qJ2Hqwgdn3-mFjzvyAVzPALh0xVB9v6EDbf4HAbqhKIx'
service_instance_id = 'crn:v1:bluemix:public:cloud-object-storage:global:a/7034cdb9c5cd4906857da0820097248a:543acec2-5392-40d2-9f54-94f323f0f402:bucket:tennisonyu-w251-hw3'
auth_endpoint = 'http://s3.us-south.cloud-object-storage.appdomain.cloud'
service_endpoint = 'http://s3.sjc.us.cloud-object-storage.appdomain.cloud'

s3 = ibm_boto3.resource('s3',
                      ibm_api_key_id=api_key,
                      ibm_service_instance_id=service_instance_id,
                      ibm_auth_endpoint=auth_endpoint,
                      config=Config(signature_version='oauth'),
                      endpoint_url=service_endpoint)


data = open('test.txt', 'rb')
s3.Bucket('tennisonyu-w251').put_object(Key='test.text', Body=data)
