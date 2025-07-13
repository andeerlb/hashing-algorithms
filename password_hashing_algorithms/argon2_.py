# %%
import argon2

time_cost = 16
memory_cost = 2**15  # 32768 KiB (32MB)
parallelism = 2
hash_len = 32
salt = b'some salt'
password = b'password'

argon2_hasher = argon2.PasswordHasher(
    time_cost=time_cost,
    memory_cost=memory_cost,
    parallelism=parallelism,
    hash_len=hash_len,
    salt_len=16 # defaults to 16
)

hashed_password = argon2_hasher.hash(password.decode('utf-8'))
print("Argon2 hash", hashed_password)

# Verify the correct password
password_is_right = argon2_hasher.verify(hashed_password, "password")
print("Password is right ", password_is_right)

# incorrect password
try:
    argon2_hasher.verify(hashed_password, "wrong password")
except argon2.exceptions.VerifyMismatchError:
    print("Password is wrong")
# %%
