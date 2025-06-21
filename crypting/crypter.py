from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import bcrypt
import string
import secrets
import html

def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            return password

def derive_key(master_password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return kdf.derive(master_password.encode())

def encrypt_password(password: str, key: bytes):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, password.encode(), None)
    return nonce, ct

def decrypt_password(nonce: bytes, cipher: bytes, key: bytes):
    aesgcm = AESGCM(key)
    pt = aesgcm.decrypt(nonce, cipher, None)
    return pt.decode()

def generate_salt():
    return os.urandom(16)

def checkExisting(input: str, database):
    existing = database.fetchAllSites()
    if input in existing:
        return True
    return False
