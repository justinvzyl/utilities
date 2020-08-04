import boto3
import base64
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


string_to_encrypt = 'STRING_TO_ENCRYPT'


def decrypt_secret_with_kms(cypher_text):
    client = boto3.client('kms')
    if cypher_text:
        decrypted_response = client.decrypt(CiphertextBlob=bytes(base64.b64decode(cypher_text)))
        return decrypted_response['Plaintext']
    else:
        raise Exception("Can't decrypt an empty string")


def encrypt_with_kms(s):
    client = boto3.client('kms')
    key_id = 'KMS_KEY_ID'
    encrypted_response = client.encrypt(KeyId=key_id, Plaintext=bytes(s))
    encrypted_string = base64.b64encode(bytes(encrypted_response['CiphertextBlob']))
    return encrypted_string


encrypted = encrypt_with_kms(string_to_encrypt)
logger.info(f'Encrypted string: {encrypted}')

decrypted = decrypt_secret_with_kms(encrypted)
logger.info(f'Decrypted string: {decrypted}')
