import boto3

import credentials
from utils import list_bucket_contents

if __name__ == "__main__":

    s3 = boto3.client(
        "s3",
        aws_access_key_id=credentials.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=credentials.AWS_SECRET_ACCESS_KEY,
        endpoint_url=credentials.ENDPOINT_URL,
    )

    list_bucket_contents(s3, "test")
