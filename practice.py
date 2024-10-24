# try:
#     hours = input("please provide your hours: ")
#     hours = int(hours)
#     print(hours)
#     print(type(hours))
#     rate = input("please provide rate: ")
#     rate = float(rate)
#     print(rate)
#     pay = (hours * rate)
#     print ("pay is:" ,pay)
# except Exception as e:
#     print(e)

    # ValueError
    # print("you entered an invalid entry")
    # print("try again")


# Dictionary of cats with their attributes
# cats = {
#     'Whiskers': {
#         'age': 3,
#         'breed': 'Siamese',
#         'color': 'Gray'
#     },
#     'Mittens': {
#         'age': 5,
#         'breed': 'Persian',
#         'color': 'White'
#     },
#     'Shadow': {
#         'age': 2,
#         'breed': 'Maine Coon',
#         'color': 'Black'
#     }
# }

# # Display information about each cat
# for cat, details in cats.items():
#     print(f"{cat} is a {details['age']} year old {details['color']} {details['breed']} cat.")
    
    
#     import boto3
# import os

# # Initialize the EC2 client
# ec2 = boto3.client('ec2')

# # Get the schedule action from environment variables
# ACTION = os.environ['ACTION']  # 'start' or 'stop'
# TAG_KEY = os.environ.get('TAG_KEY', 'Scheduler')  # Default tag key is 'Scheduler'

# def lambda_handler(event, context):
#     # Filter instances based on the tag key and action (start or stop)
#     instances = get_instances_by_tag(TAG_KEY, ACTION)

#     if not instances:
#         return f'No instances found for action: {ACTION}'
    
#     # Perform the start or stop action
#     if ACTION == 'start':
#         start_instances(instances)
#     elif ACTION == 'stop':
#         stop_instances(instances)
    
#     return f'{ACTION.capitalize()}ed instances: {instances}'

# def get_instances_by_tag(tag_key, action):
#     # Retrieve instances with the specific tag (start/stop)
#     filters = [
#         {
#             'Name': f'tag:{tag_key}',
#             'Values': [action]
#         },
#         {
#             'Name': 'instance-state-name',
#             'Values': ['running' if action == 'stop' else 'stopped']
#         }
#     ]
    
#     response = ec2.describe_instances(Filters=filters)
#     instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    
#     return instances

# def start_instances(instance_ids):
#     if instance_ids:
#         print(f"Starting instances: {instance_ids}")
#         ec2.start_instances(InstanceIds=instance_ids)

# def stop_instances(instance_ids):
#     if instance_ids:
#         print(f"Stopping instances: {instance_ids}")
#         ec2.stop_instances(InstanceIds=instance_ids)


# Explanation:
# Environment Variables:

# ACTION: You can set it to "start" or "stop" when scheduling the Lambda function.
# TAG_KEY: (optional) The key used to filter instances by their tags (default: "Scheduler").
# get_instances_by_tag():

# Filters EC2 instances based on the tag key (Scheduler by default) and the action (start or stop).
# start_instances() / stop_instances():

# These functions handle starting and stopping instances, respectively, using the EC2 API.
# Deployment Steps:
# Create IAM Role: Ensure the Lambda execution role has the following permissions for EC2 actions:

# json
# Copy code
# {
#     "Effect": "Allow",
#     "Action": [
#         "ec2:DescribeInstances",
#         "ec2:StartInstances",
#         "ec2:StopInstances"
#     ],
#     "Resource": "*"
# }
# Create Lambda Function:

# Open AWS Lambda and create a new function.
# Choose the execution role created above.
# Copy and paste the Python code.
# Set Environment Variables:

# In the Lambda function, set the environment variable ACTION to either start or stop depending on the function's purpose.
# Optionally set TAG_KEY if you're using a different tag key than Scheduler.
# Set CloudWatch Rule:

# Go to CloudWatch > Rules and create a new rule.
# Use the "Schedule" option to specify when you want to trigger the function (e.g., every day at 8 AM to start instances).
# Set the rule to trigger the Lambda function with the appropriate environment variables (like starting or stopping).
# Cost-saving Example:
# Tag your instances:
# Add a tag like Scheduler=start or Scheduler=stop to EC2 instances.
# Create two Lambda functions—one to start instances (with ACTION=start) and another to stop instances (with ACTION=stop).
# Schedule the functions with CloudWatch, such as starting instances at 8 AM and stopping them at 6 PM.
# By doing this, your EC2 instances will automatically start and stop based on your schedule, helping you optimize costs.


# python inbuilt functions
# input()
# type()
# bool()
# int()
# float()
# print()

# name = input("what is your name?: ")
# print(name)
# print("my name is: " ,name)
# print("Hi " + name)
# favorite_color = input("what is your favorite color?: ")
# print(name,  "likes",  favorite_color)

try:
    height = input("what is your height?: (cm)")
    height = float(height)
    weight = input("what is your weight? (cm)")
    weight = float(weight)
    print(height,"cm")
    print(weight,"cm")
    result = weight * height 
    print("the result of weight * height is:", result, "cm")
except Exception as e :
    print(e)
    # print("You entered and invalid value", "Try again")
    print("something went wrong")







