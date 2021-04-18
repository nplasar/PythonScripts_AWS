import boto3

aws_mgt_con = boto3.session.Session(profile_name = "nplasar")
ec2_con_re = aws_mgt_con.resource(service_name="ec2", region_name="eu-west-2")

Tags_Spec=[
            {
                'ResourceType':'instance',
                'Tags':[
                        {
                            'Key':'Name',
                            'Value':'Dev'
                            
                            
                        }
                    ]
                }
            ]
response = ec2_con_re.create_instances(
        ImageId='ami-0fbec3e0504ee1970',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        TagSpecifications=Tags_Spec
        )



