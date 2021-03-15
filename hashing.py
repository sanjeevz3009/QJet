import hashlib
import os 

userInput = input("Enter password to hash: ")
print(userInput)
hashInput = userInput.encode()
print(hashInput)

salt = os.urandom(32)
print("Salt: ", salt.hex())

print("\n")


hashed = hashlib.pbkdf2_hmac("sha256", hashInput, salt, 100000)
print(hashed)
print(hashed.hex())
print(len(hashed.hex()))




