import boto3


aws_mgt_con = boto3.session.Session (profile_name = "NAMEOFYOURPROFILE")
iam_con_client = aws_mgt_con.client (service_name = "iam", region_name = "eu-west-2")
ec2_con_client = aws_mgt_con.client (service_name = "ec2", region_name = "eu-west-2")
s3_con_client = aws_mgt_con.client (service_name = "s3", region_name = "eu-west-2")

#Reterive list of users from IAM
response = iam_con_client.list_users()
for each_user_name in response['Users']:
    print (each_user_name['UserName'])

#Reterive list of ec2 insatnces
response_ec2 = ec2_con_client.describe_instances()
for each_ec2_client in response_ec2['Reservations']:
    
    for each_ec2_client_res in each_ec2_client['Instances']:
        print ("The Instance Id is {}: \n Image Id is {}".format(each_ec2_client_res['InstanceId'],each_ec2_client_res['ImageId'])
#Reterive list of S3 buckets
response_s3 = s3_con_client.list_buckets()
for each_buck_name in response_s3['Buckets']:
    print (each_buck_name['Name'])
