import os

def create_bucket(service_client, bucket_name):

    try:
        service_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created")
        service_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={"Status": "Enabled"}
        )
        print(f"Versioning enabled for '{bucket_name}'.")
    except service_client.exceptions.BucketAlreadyExists as e:
        print(f"Bucket already exists: {e}")
    except service_client.exceptions.BucketAlreadyOwnedByYou:
        print(f"Bucket '{bucket_name}' already owned by you.")


def list_bucket_contents(service_client, bucket_name):
    try:
        response = service_client.list_objects_v2(Bucket=bucket_name)
        if "Contents" in response:
            print(f"\nContents of bucket '{bucket_name}':")
            for obj in response["Contents"]:
                print(f" - {obj['Key']} (Size: {obj['Size']} bytes)")
        else:
            print(f"\nBucket '{bucket_name}' is empty.")
    except service_client.exceptions.NoSuchBucket:
        print(f"Bucket '{bucket_name}' does not exist.")


def upload_folder(service_client, bucket_name, folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                key = os.path.relpath(file_path, start=folder_path).replace("\\", "/")
                service_client.upload_file(file_path, bucket_name, key)
                print(f"Uploaded {file_path} as {key}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")