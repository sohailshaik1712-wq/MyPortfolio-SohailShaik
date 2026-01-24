import bcrypt

# Replace with your desired admin password
password = "moundlitch21"  # Change this!
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
print(f"Use this hash in your config:")
print(hashed.decode())
