# %%
import bcrypt

password = b"mysecretpassword123"

# The 'rounds' parameter in gensalt() determines the computational cost.
# Higher rounds mean more secure but slower hashing. Default is 12.
salt = bcrypt.gensalt(rounds=12)

# 4. Hash the password using the salt
hashed_password = bcrypt.hashpw(password, salt)

print(f"Original password: {password.decode('utf-8')}")
print(f"Hashed password: {hashed_password.decode('utf-8')}")

# Verify a password against the stored hash
# Simulate a user entering their password for login
entered_password = "mysecretpassword123"
entered_byte_password = entered_password.encode('utf-8')

print(f"\nTrying to authenticate with password: {entered_password}")
if bcrypt.checkpw(entered_byte_password, hashed_password):
    print("Password match! User authenticated.\n")

# Example with an incorrect password
incorrect_password = "wrongpassword"
print(f"Trying to authenticate with incorrect password: {incorrect_password}")
incorrect_byte_password = incorrect_password.encode('utf-8')

if bcrypt.checkpw(incorrect_byte_password, hashed_password):
    print("Password match! (This should not happen for incorrect password)")
else:
    print("Incorrect password. Authentication failed (as expected).")
# %%
