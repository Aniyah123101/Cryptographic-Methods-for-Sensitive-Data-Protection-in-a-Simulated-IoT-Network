import pyotp
import time

# Ensure the secret key matches exactly with the one used to set up Google Authenticator
secret = "2B64AQCAYBPVFZVOSPFDHYP4M6DVQUVW"  # Replace with your actual base32 secret key

# Create a TOTP object using the secret key
totp = pyotp.TOTP(secret)

# Print the current OTP (This should match the one shown in Google Authenticator)
current_otp = totp.now()
print(f"Your secret key is: {secret}")
print(f"Current OTP: {current_otp}")

# Verify the OTP manually entered
user_input = input("Enter the OTP from Google Authenticator: ").replace(" ", "")

def validate_otp(user_input_otp):
    """
    Validates the OTP entered by the user against the TOTP.
    """
    if totp.verify(user_input_otp):
        print("OTP is valid!")
    else:
        print("Invalid OTP. Please check the time and secret key.")



# Validate user input
validate_otp(user_input)

# Verify with specific TOTP configuration
totp = pyotp.TOTP(secret, interval=30, digits=6)

