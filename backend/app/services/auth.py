from datetime import datetime, timedelta, timezone

from core.config import ALGORITHM, SECRET_KEY
from core.security import verify_password
from jose import jwt


def authenticate(username, password, admin_user, admin_hash):
    if username != admin_user:
        return False

    print(f"DEBUG: Hash starts with: {admin_hash[:20] if admin_hash else 'None'}...")
    print(f"DEBUG: Hash length: {len(admin_hash) if admin_hash else 0}")
    return verify_password(password, admin_hash)


def create_token(data: dict, expires: int):
    to_encode = data.copy()

    # Always use UTC time for JWT
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
