#!/usr/bin/env python3

##########################################################
# Created: Esther Ezekiel                   #
##########################################################

import os
from typing import Union
from datetime import datetime

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("REGION")


# Initialize S3 Client
def get_client(service: str) -> boto3.client:
    """

    :param service: example -> s3, ec2, lambda
    :return: boto3.Session
    """
    return boto3.client(
        service,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )


def upload_file(file_path: str, bucket_name: str, object_name: str = None) -> Union[str, bool]:
    """
    Upload a file to an S3 bucket.

    :param file_path: Local path to the file
    :param bucket_name: The S3 bucket name
    :param object_name: The name of the file in the bucket (if None, the file name will be used)
    :return: True if file was uploaded, else False
    """

    if not object_name:
        object_name = os.path.basename(file_path)

    s3_client = get_client("s3")

    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File uploaded successfully to {bucket_name}/{object_name}")
        return True
    except (NoCredentialsError, PartialCredentialsError):
        return "Credentials are not available or incomplete."
    except Exception as e:
        return f"Error uploading file: {str(e)}"


def download_file(bucket_name, object_name, file_path):
    """
    Download a file from an S3 bucket.

    :param bucket_name: The S3 bucket name
    :param object_name: The name of the file in the bucket
    :param file_path: Local path to save the file
    :return: True if the file was downloaded, else False
    """
    s3_client = get_client("s3")

    try:
        s3_client.download_file(bucket_name, object_name, file_path)
        print(f"File downloaded successfully from {bucket_name}/{object_name} to {file_path}")
        return True
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
    return False

