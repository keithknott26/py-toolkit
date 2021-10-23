import boto3 

kms = boto3.client('kms')

def decrypt():
    """Decrypt attempts to decrypt given data and KMS automatically finds the correct key within encrypted data."""
    ret = kms.decrypt()

    decrypted_data = ""
    print("Decrypted data: {}".format(decrypted_data.replace('\n', '')))
    
    return decrypted_data   