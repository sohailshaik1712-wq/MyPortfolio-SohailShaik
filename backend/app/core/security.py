import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def verify_password(plain: str, hashed: str) -> bool:
    try:
        # 1. Handle literal "b'hash'" string corruption
        if hashed.startswith("b'") or hashed.startswith('b"'):
            hashed = hashed[2:-1]

        # 2. Re-verify format after cleaning
        if not hashed.startswith(("$2a$", "$2b$", "$2y$")):
            print(f"Warning: Invalid bcrypt hash format: {hashed[:10]}...")
            return False

        return bcrypt.checkpw(plain.encode(), hashed.encode())
    except Exception as e:
        print(f"Auth Error: {e}")
        return False
