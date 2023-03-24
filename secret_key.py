import secrets
import base64
from cryptography.fernet import Fernet


def encrypted_key(): 
    # Generates a 32-byte secret key
    secret_key = secrets.token_bytes(32)

    # Securely encode the key in base64
    encoded_key = base64.urlsafe_b64encode(secret_key)

    # Creates a Fernet object with the secret key
    fernet = Fernet(encoded_key)

    return encoded_key

