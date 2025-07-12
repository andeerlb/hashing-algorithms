# %%
## sha-2 hash-224
import hashlib

def generate_sha_hash(input_string):
    return hashlib.sha224(input_string.encode('utf-8')).hexdigest()

string_to_hash = "Anderson"
hashed_value = generate_sha_hash(string_to_hash)

print(f"hash224: {hashed_value}")
# %%
## sha-2 hash-256
import hashlib

def generate_sha_hash(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()

string_to_hash = "Anderson"
hashed_value = generate_sha_hash(string_to_hash)

print(f"hash256: {hashed_value}")
# %%
## sha-2 hash-384
import hashlib

def generate_sha_hash(input_string):
    return hashlib.sha384(input_string.encode('utf-8')).hexdigest()

string_to_hash = "Anderson"
hashed_value = generate_sha_hash(string_to_hash)

print(f"hash384: {hashed_value}")
# %%
## sha-2 hash-512
import hashlib

def generate_sha_hash(input_string):
    return hashlib.sha512(input_string.encode('utf-8')).hexdigest()

string_to_hash = "Anderson"
hashed_value = generate_sha_hash(string_to_hash)

print(f"hash512: {hashed_value}")
# %%
