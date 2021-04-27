import boto3

aws_mag_con = boto3.session.Session(profile_name="NAMEOFYOURPROFILE")
ec2_con_res = aws_mag_con.resource(service_name="ec2",region_name="eu-west-2")
ec2_con_cli = aws_mag_con.client(service_name="ec2",region_name="eu-west-2")

#Using Resource
#ec2_ins_obj = ec2_con_res.Instance("i-0cff5fb2a61c96e5a")
#print("Instance is starting")
#ec2_ins_obj.start()
#print(dir(ec2_ins_obj))
#ec2_ins_obj.wait_until_running()
##print("Instance is now running")

#Using Waiter
print("Instance is starting")
ec2_con_cli.start_instances(InstanceIds=['i-0cff5fb2a61c96e5a'])
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-0cff5fb2a61c96e5a'])
print("Instance is now running")
