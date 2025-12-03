import sys

import boto3

import credentials
from utils import upload_folder

if __name__ == "__main__":

    args = sys.argv

    s3 = boto3.client(
        "s3",
        aws_access_key_id=credentials.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=credentials.AWS_SECRET_ACCESS_KEY,
        endpoint_url=credentials.ENDPOINT_URL,
    )

    upload_folder(s3, bucket_name="test", folder_path="test_data_A")
    # upload_folder(s3, bucket_name="test", folder_path="test_data_B")