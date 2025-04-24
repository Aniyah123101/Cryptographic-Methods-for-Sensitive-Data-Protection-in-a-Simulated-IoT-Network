import pyotp

# Use the secret key generated earlier
secret = "Your_Secret_Key_Here"  # Replace with the actual secret key
totp = pyotp.TOTP(secret)

def validate_otp(user_input_otp):
    """
    Validates the OTP entered by the user against the TOTP.
    """
    if totp.verify(user_input_otp):
        print("OTP is valid!")
        return True
    else:
        print("Invalid OTP.")
        return False

# Example usage
user_input = input("Enter the OTP from Google Authenticator: ")
validate_otp(user_input)
