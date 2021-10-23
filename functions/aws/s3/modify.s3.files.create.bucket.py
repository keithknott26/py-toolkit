import os
import boto3
import logging

logger = logging.getLogger(__name__)


class S3Exception(Exception):
    pass


def get_s3_client(access_key, secret, endpoint=None, region=None):
    return boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret,
        endpoint_url=endpoint,
        region_name=region,
        # config=boto3.session.Config(signature_version='s3v4'),
    )


def get_s3_resource(access_key, secret, endpoint=None, region=None):
    return boto3.resource(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret,
        endpoint_url=endpoint,
        region_name=region,
        # config=boto3.session.Config(signature_version='s3v4'),
    )


class S3Operator(object):
    def __init__(self, access_key=None, secret=None, endpoint=None, region=None):
        self.client = get_s3_client(
            access_key,
            secret,
            endpoint=endpoint,
            region=region
        )
        self.resource = get_s3_resource(
            access_key,
            secret,
            endpoint=endpoint,
            region=region
        )

    def upload_file(self, localpath, bucket_name, object_name=None):
        if not os.path.exists(localpath):
            return False
        object_name = object_name or os.path.basename(localpath)
        try:
            self.client.upload_file(localpath, bucket_name, object_name)
        except S3Exception as ex:
            logger.error(ex)
        return True

    def upload_file_blob(self, file_blob, bucket_name, object_name):
        try:
            self.client.put_object(Bucket=bucket_name, Key=object_name, Body=file_blob)
        except S3Exception as ex:
            logger.error(ex)
        return True

    def download_file_blob(self, bucket_name, object_name):
        obj = self.resource.Object(bucket_name, object_name)
        body = obj.get()
        blob = body['Body'].read()
        return blob

    def get_signed_url(self, bucket_name, object_name, expiredin=86400, httpmethod=None):
        url = self.client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_name,
            },
            ExpiresIn=expiredin,
            HttpMethod=httpmethod,
        )
        return url

    def create_bucket_if_not_exists(self, bucket_name):
        existing = [b['Name'] for b in self.client.list_buckets()['Buckets']]
        if bucket_name not in existing:
            self.resource.create_bucket(Bucket=bucket_name)
            print('Created bucket:', str(bucket_name))
        return self.resource.Bucket(bucket_name).creation_date

    def delete_bucket(self, bucket_name):
        """
        Only used in testing environment
        """
        existing = [b['Name'] for b in self.client.list_buckets()['Buckets']]
        if bucket_name in existing:
            bucket = self.resource.Bucket(bucket_name)
            _ = [key.delete() for key in bucket.objects.all()]
            bucket.delete()

    def list_objects_under_folder(self, bucket_name, folder_path=None):
        obj_keys = []
        is_truncated = False
        while is_truncated:
            objects = self.client.list_objects(Bucket=bucket_name, Prefix=folder_path, MaxKeys=1000)
            obj_keys += [obj['Key'] for obj in objects.get('Contents', [])]
            is_truncated = objects.get('IsTruncated', False)
        return obj_keys

    def list_objects(self, bucket_name, path_prefix=None):
        if path_prefix:
            keys = [obj.key for obj in self.resource.Bucket(bucket_name).objects.filter(Prefix=path_prefix)]
        else:
            keys = [obj.key for obj in self.resource.Bucket(bucket_name).objects.all()]
        return keys
