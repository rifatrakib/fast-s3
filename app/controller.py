import json
import boto3


def fetch_data_from_s3(payload, access_key, secret_key):
    s3 = boto3.client(
        "s3", aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    bucket_name = payload.bucket_name
    directory = payload.directory
    file_name = directory.split("/")[-1]
    
    s3.download_file(bucket_name, directory, f"app/downloads/{file_name}")
    with open(f"app/downloads/{file_name}") as handle:
        data = json.loads(handle.read())
    
    response = {
        "data": data
    }
    
    return response
