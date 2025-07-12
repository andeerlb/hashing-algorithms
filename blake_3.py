# %% 
# basic usage
import blake3

data = b"Anderson"
hash_object = blake3.blake3(data)
hash_hex = hash_object.hexdigest()
print(f"Hash: {hash_hex}")
# %%
# Keyed hashing
import blake3

my_key = b"my_key"
keyed_hash = blake3.blake3(key=my_key)
keyed_hash.update(b"Sensitive information.")
print(f"Keyed Hash: {keyed_hash.hexdigest()}")
# %%
import blake3

extended_output = blake3.blake3(b"input_for_xof").digest(length=64)
print(f"Extended Output: {extended_output.hex()}")

seeked_output = blake3.blake3(b"input_for_xof").digest(length=10, seek=10)
print(f"Seeked Output (bytes 10-19): {seeked_output.hex()}")
# %%
import blake3

large_input = bytearray(10 * 1024 * 1024)  # 10 MB of data

hash_auto_threads = blake3.blake3(large_input, max_threads=2).hexdigest()
print(f"Hash: {hash_auto_threads}")
# %%
