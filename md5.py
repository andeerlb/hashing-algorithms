# %%
## creating a md5
import hashlib

def get_md5_of_string(input_string):
    md5_hash = hashlib.md5(input_string.encode('utf-8')).hexdigest()
    return md5_hash

string_to_hash = "Anderson"
md5_result = get_md5_of_string(string_to_hash)
print(f"hash of \"{string_to_hash}\": {md5_result}")
# %%
## simulating a md5 colission
import hashlib
# Source: https://www.johndcook.com/blog/2024/03/20/md5-hash-collision/

string1 = b"TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
string2 = b"TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"

if(string1 != string2):
    print("Input strings are different\n")

hash1 = hashlib.md5(string1).hexdigest()
hash2 = hashlib.md5(string2).hexdigest()

print(f"MD5 Hash 1: {hash1}\n")
print(f"MD5 Hash 2: {hash2}")

if hash1 == hash2:
    print("\nMD5 Collision Detected")
# %%
