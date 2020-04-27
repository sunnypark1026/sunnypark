"""
Created on Sun Apr 19 22:41:10 2020

@author: sunhee park

"""

import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIA3XGO4X54GB2LMXN7'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('local_file', 'information-arch', 's3_file_name')

print("Done! with the uploud")
