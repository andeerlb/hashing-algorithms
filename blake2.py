# %%
## Can produce a hash digest of up to 64 bytes (512 bits). 
import hashlib

string_to_hash = b"Anderson"
blake_object = hashlib.blake2b(digest_size=64)
blake_object.update(string_to_hash)
hash_result = blake_object.hexdigest()

print(f"Hash blake2b: {hash_result}")
print(f"Digest Size: {blake_object.digest_size} bytes")

# %%
## Can produce a hash digest of up to 32 bytes (256 bits). 
import hashlib

string_to_hash = b"Anderson"
blake_object = hashlib.blake2s(digest_size=32)
blake_object.update(string_to_hash)
hash_result = blake_object.hexdigest()

print(f"Hash blake2s: {hash_result}")
print(f"Digest Size: {blake_object.digest_size} bytes")
# %%
