# %%
import zlib

string_to_hash = "Anderson"
str_hash = zlib.crc32(string_to_hash.encode('utf-8'))
print(f"hash of '{string_to_hash}': {str_hash}")

# %%
import zlib

file_hash = 0
with open("../files/test_file.txt",'rb') as f:
    while True:
        chunk = f.read(4096)  # Read 4KB at a time
        if not chunk:
            break
        file_hash = zlib.crc32(chunk)

print(f"hash of 'test_file.txt': {file_hash}")
# %%
