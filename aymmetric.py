from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate private & public key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Input message
message = b"Top secret RSA message!"

# Encrypt with public key
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
)

# Decrypt with private key
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
)

# Show results
print("Asymmetric Encryption")
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")
print(f"Original Message: {message.decode()}")
print(f"Encrypted Message (bytes): {encrypted_message}")
print(f"Decrypted Message: {decrypted_message.decode()}")