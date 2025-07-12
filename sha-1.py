# %%
## creating a sha-1
import hashlib
string_to_hash = "Anderson"
hash = hashlib.sha1(string_to_hash.encode()).hexdigest()
print(hash)
# %%
import hashlib

def check_if_files_are_different():
    with open("./files/shattered-1.pdf", "rb") as f1, open("./files/shattered-2.pdf", "rb") as f2:
        if f1.read() != f2.read():
            print("The files are different\n")

def sha1_hash(filename):
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

check_if_files_are_different()
hash1 = sha1_hash("./files/shattered-1.pdf")
hash2 = sha1_hash("./files/shattered-2.pdf")

print("hash1: ", hash1)
print("hash2: ", hash2)

if hash1 == hash2:
    print("\nCollision detected")
# %%
