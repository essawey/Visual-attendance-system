import random
import string

def generate_otp():
    """
    Generate a random one-time password (OTP) of the 6 length.

    Returns:
    - str: The generated OTP.
    """
    characters = string.digits + string.ascii_letters  # Include digits and letters
    characters = characters.upper()
    return ''.join(random.choice(characters) for _ in range(6))
