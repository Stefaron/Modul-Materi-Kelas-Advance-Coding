import re

def validasi_username(username):
    pattern = r"^[a-zA-Z0-9_]{3,15}$"
    return re.match(pattern, username) is not None

print(validasi_username("user_123"))  # Output: True
print(validasi_username("u"))         # Output: False
