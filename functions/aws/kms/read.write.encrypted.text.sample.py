
   
import boto3 
import base64
import click 
import random

kms = boto3.client('kms')

@click.group()
def main():
    """ Simple utility to encrypt/decrypt data via AWS KMS 
    \b
    Common Usage:
    
        python simple_encrypt.py encrypt "my super secret data"
        python simple_encrypt.py decrypt "my super secret data"
    Optional Usage - Using Encryption Context:
        python simple_encrypt.py encrypt "my super secret data" -c "MyNewCustomer"
        
        python simple_encrypt.py decrypt "my super secret data" -c "MyNewCustomer"
    More info about KMS usage: http://amzn.to/2ifycIh
    """
    pass

@main.command(short_help='encrypted input data with or without context')
@click.argument("data")
@click.option("-k", "--key", default="alias/local_lambda", help="KMS Key ID/alias used for this operation")
@click.option("-c", "--context", help="Define encryption context (Customer, Service, etc.)")
def encrypt(key, data, context):
    """Encrypt uses KMS Key provided (or attempts default value) to encrypt given data."""
    if context:
        ret = kms.encrypt(KeyId=key, Plaintext=data, EncryptionContext={'CustomContext': '{}'.format(context)})
    else:
        ret = kms.encrypt(KeyId=key, Plaintext=data)
    
    encrypted_data = base64.encodestring(ret.get('CiphertextBlob'))
    click.echo("Encrypted data: {}".format(encrypted_data.replace('\n', '')))
    
    return encrypted_data

@main.command(short_help='decrypted input data with or without context')
@click.argument("data")
@click.option("-c", "--context", help="Define encryption context (Customer, Service, etc.)")
def decrypt(data, context):
    """Decrypt attempts to decrypt given data and KMS automatically finds the correct key within encrypted data."""
    if context:
        ret = kms.decrypt(CiphertextBlob=base64.decodestring(data), EncryptionContext={'CustomContext': '{}'.format(context)})
    else:
        ret = kms.decrypt(CiphertextBlob=base64.decodestring(data))

    decrypted_data = ret.get('Plaintext')
    click.echo("Decrypted data: {}".format(decrypted_data.replace('\n', '')))
    
    return decrypted_data

if __name__ == '__main__':
    main()