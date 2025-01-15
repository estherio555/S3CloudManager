
#################################################
# Created: Esther Ezekiel

# Print environment variables
import os
print(os.environ['AWS_SECRET_ACCESS_KEY'])

import boto3

#Add new environment variables from .env
from dotenv import load_dotenv
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv("REGION")

# print(AWS_REGION)

# Create an S3 client
s3 = boto3.client('s3')

# List objects in a specific S3 bucket
bucket_name = 'your-bucket-name'
response = s3.list_objects_v2(Bucket=bucket_name)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
