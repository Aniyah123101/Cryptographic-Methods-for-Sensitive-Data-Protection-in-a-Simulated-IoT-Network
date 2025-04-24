from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import base64

# AES Encryption and Decryption
def aes_encrypt_decrypt(data):
    # Generate a random 16-byte AES key and IV
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the data to be a multiple of the block size
    padded_data = pad(data.encode(), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    encoded_encrypted_data = base64.b64encode(encrypted_data).decode()

    # Decrypt the data
    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_data = decipher.decrypt(base64.b64decode(encoded_encrypted_data))
    decrypted_data = unpad(decrypted_padded_data, AES.block_size).decode()

    return encoded_encrypted_data, decrypted_data

# DES Encryption and Decryption
def des_encrypt_decrypt(data):
    # Generate a random 8-byte DES key and IV
    key = get_random_bytes(8)
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)

    # Pad the data to be a multiple of the block size
    padded_data = pad(data.encode(), DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    encoded_encrypted_data = base64.b64encode(encrypted_data).decode()

    # Decrypt the data
    decipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_padded_data = decipher.decrypt(base64.b64decode(encoded_encrypted_data))
    decrypted_data = unpad(decrypted_padded_data, DES.block_size).decode()

    return encoded_encrypted_data, decrypted_data

# RSA Encryption and Decryption
def rsa_encrypt_decrypt(data):
    # Generate an RSA key pair
    key = RSA.generate(2048)
    public_key = key.publickey()

    # Encrypt the message using the public key
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher_rsa.encrypt(data.encode())
    encoded_encrypted_data = base64.b64encode(encrypted_data).decode()

    # Decrypt the message using the private key
    cipher_rsa = PKCS1_OAEP.new(key)
    decrypted_data = cipher_rsa.decrypt(base64.b64decode(encoded_encrypted_data)).decode()

    return encoded_encrypted_data, decrypted_data

# Main function to demonstrate the encryption and decryption
def main():
    sample_data = "This is a sample message to be encrypted."

    # Test AES Encryption and Decryption
    aes_encrypted, aes_decrypted = aes_encrypt_decrypt(sample_data)
    print(f"\nAES Encrypted: {aes_encrypted}")
    print(f"AES Decrypted: {aes_decrypted}")

    # Test DES Encryption and Decryption
    des_encrypted, des_decrypted = des_encrypt_decrypt(sample_data)
    print(f"\nDES Encrypted: {des_encrypted}")
    print(f"DES Decrypted: {des_decrypted}")

    # Test RSA Encryption and Decryption
    rsa_encrypted, rsa_decrypted = rsa_encrypt_decrypt(sample_data)
    print(f"\nRSA Encrypted: {rsa_encrypted}")
    print(f"RSA Decrypted: {rsa_decrypted}")

# Run the main function
if __name__ == "__main__":
    main()
