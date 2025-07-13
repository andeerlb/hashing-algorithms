# %%
import zlib

string_to_hash = "Anderson"
checksum_string = zlib.crc32(string_to_hash.encode('utf-8'))
print(f"hash of '{string_to_hash}': {checksum_string}")

# %%
import zlib

file_checksum = 0
with open("../files/test_file.txt",'rb') as f:
    while True:
        chunk = f.read(4096)  # Read 4KB at a time
        if not chunk:
            break
        file_checksum = zlib.crc32(chunk, file_checksum)

print(f"hash of 'test_file.txt': {file_checksum}")
# %%
