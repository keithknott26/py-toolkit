import boto3 
import base64

kms = boto3.client('kms')

def encrypt():
    """Encrypt uses KMS Key provided (or attempts default value) to encrypt given data."""
    ret = kms.encrypt()
    
    encrypted_data = 
    print("Encrypted data: {}".format(encrypted_data.replace('\n', '')))
    
    return encrypted_data