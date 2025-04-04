import random
import string

def generate_email(domain='gmail.com'):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@{domain}"

temp_email = generate_email()
print(f"temporary email: {temp_email}")