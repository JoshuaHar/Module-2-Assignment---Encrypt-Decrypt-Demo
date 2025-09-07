from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Input message
message = b"Hello, this is a secret message!"

# Encrypt
encrypted_message = cipher.encrypt(message)

# Decrypt
decrypted_message = cipher.decrypt(encrypted_message)

# Show results
print("Symmetric Encryption")
print(f"Key: {key.decode()}")
print(f"Original Message: {message.decode()}")
print(f"Encrypted Message: {encrypted_message.decode()}")
print(f"Decrypted Message: {decrypted_message.decode()}")