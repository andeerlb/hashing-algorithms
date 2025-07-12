# %%
import hashlib

def generate_sha3_hash(input_string):
    return hashlib.sha3_224(input_string.encode('utf-8')).hexdigest()

string_to_hash = "Anderson"
hash_result = generate_sha3_hash(string_to_hash)
print(f"hash256: {hash_result}")

# %%
import hashlib

def generate_sha3_hash(input_string):
    return hashlib.sha3_256(input_string.encode('utf-8')).hexdigest()

string_to_hash = "Anderson"
hash_result = generate_sha3_hash(string_to_hash)
print(f"hash256: {hash_result}")
# %%
import hashlib

def generate_sha3_hash(input_string):
    return hashlib.sha3_384(input_string.encode('utf-8')).hexdigest()

string_to_hash = "Anderson"
hash_result = generate_sha3_hash(string_to_hash)
print(f"hash256: {hash_result}")
# %%
import hashlib

def generate_sha3_hash(input_string):
    return hashlib.sha3_512(input_string.encode('utf-8')).hexdigest()

string_to_hash = "Anderson"
hash_result = generate_sha3_hash(string_to_hash)
print(f"hash256: {hash_result}")
# %%
