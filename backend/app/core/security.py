import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def verify_password(plain: str, hashed: str) -> bool:
    try:
        # Ensure hashed password is properly formatted
        if not hashed.startswith(("$2a$", "$2b$", "$2y$")):
            print(f"Warning: Invalid bcrypt hash format: {hashed[:20]}...")
            return False

        return bcrypt.checkpw(plain.encode(), hashed.encode())
    except ValueError as e:
        print(f"Password verification error: {e}")
        return False
