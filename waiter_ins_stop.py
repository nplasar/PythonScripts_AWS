import boto3

aws_mag_con = boto3.session.Session(profile_name="NAMEOFYOURPROFILE")
ec2_con_res = aws_mag_con.resource(service_name="ec2",region_name="eu-west-2")
ec2_con_cli = aws_mag_con.client(service_name="ec2",region_name="eu-west-2")


print("Instance is stopping")
ec2_con_cli.stop_instances(InstanceIds=['i-0cff5fb2a61c96e5a'])
waiter=ec2_con_cli.get_waiter('instance_stopped')
waiter.wait(InstanceIds=['i-0cff5fb2a61c96e5a'])
print("Instance is now stopped")
