import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME=os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL="https://travac.nyc3.digitaloceanspaces.com"

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'

AWS_S3_SIGNATURE_VERSION = 's3v4'

STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)


DEFAULT_FILE_STORAGE = "server.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "server.cdn.backends.StaticRootS3Boto3Storage"