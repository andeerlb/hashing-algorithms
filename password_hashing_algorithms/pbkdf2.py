# %%
import hashlib
import os

def hash_password(password: str, salt: bytes = None, iterations: int = 260000) -> bytes:
    if salt is None:
        salt = os.urandom(16)

    derived_key = hashlib.pbkdf2_hmac(
        'sha256',          # Hashing algorithm (e.g., 'sha256', 'sha512')
        password.encode('utf-8'),  # Password must be bytes
        salt,              # Salt must be bytes
        iterations,        # Number of iterations
        dklen=32           # Desired length of the derived key in bytes (e.g., 32 for SHA256)
    )
    return salt + derived_key

def verify_password(stored_hash: bytes, input_password: str, iterations: int = 260000) -> bool:
    salt = stored_hash[:16]  # Extract the salt (first 16 bytes)
    stored_derived_key = stored_hash[16:]  # Extract the derived key

    # Re-derive the key using the input password and extracted salt
    re_derived_key = hashlib.pbkdf2_hmac(
        'sha256',
        input_password.encode('utf-8'),
        salt,
        iterations,
        dklen=32
    )
    return re_derived_key == stored_derived_key

user_password = "mySecretPassword123!"

hashed_password_data = hash_password(user_password)
print(f"Hashed password (salt + derived key in hex): {hashed_password_data.hex()}")

if verify_password(hashed_password_data, user_password):
    print("Password verification successful!")

if not verify_password(hashed_password_data, "wrongPassword"):
    print("Incorrect password verification failed (as expected).")
# %%
