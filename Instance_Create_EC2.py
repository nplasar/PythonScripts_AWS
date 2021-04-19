import boto3
aws_mag_con = boto3.session.Session(profile_name="NAMEOFYOURPROFILE")
aws_ec2_con = aws_mag_con.resource(service_name='ec2', region_name='eu-west-2')

tag_spec_vpc = [
            {
                'ResourceType':'vpc',
                'Tags':[
                        {
                            'Key':'Name',
                            'Value':'Comp_Internal_VPC'
                        }
                       ]
            }
           ]
res_vpc = aws_ec2_con.create_vpc(
            CidrBlock = '10.0.0.0/16',
            TagSpecifications = tag_spec_vpc
        )
tag_spec_subnet = [
                    {
                        'ResourceType':'subnet',
                        'Tags':[
                                {
                                    'Key':'Name',
                                    'Value':'Public_SubnetA'                                                                                                                                    }                                
                                ]
                    }
                ]

res_subnet = aws_ec2_con.create_subnet(
                VpcId = res_vpc.id,
                CidrBlock = '10.0.0.0/24',
                TagSpecifications = tag_spec_subnet
                )

tag_spec_ec2 = [
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
res_instance = aws_ec2_con.create_instances(
                ImageId='ami-0fbec3e0504ee1970',
                InstanceType='t2.micro',
                MaxCount=1,
                MinCount=1,
                TagSpecifications=tag_spec_ec2,
                SubnetId=res_subnet.id
                )
