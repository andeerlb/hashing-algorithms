# %%
import zlib

string_to_hash = "Anderson"
hash = zlib.adler32(string_to_hash.encode('utf-8'))
print(f"hash: {hash}")


# %%
import zlib

file_checksum = 0
with open("../files/test_file.txt",'rb') as f:
    while True:
        chunk = f.read(4096)  # Read 4KB at a time
        if not chunk:
            break
        file_checksum = zlib.adler32(chunk)

print(f"hash of 'test_file.txt': {file_checksum}")
# %%
