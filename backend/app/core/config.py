import os

from dotenv import load_dotenv

load_dotenv()


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value


# Required config
ADMIN_USERNAME: str = _require_env("ADMIN_USERNAME")
ADMIN_PASSWORD_HASH: str = _require_env("ADMIN_PASSWORD_HASH")
SECRET_KEY: str = _require_env("SECRET_KEY")

# Optional
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

# DEBUG - Add these lines temporarily
print("=" * 60)
print("CONFIG DEBUG INFO:")
print(f"Username: {ADMIN_USERNAME}")
print(f"Hash: {ADMIN_PASSWORD_HASH}")
print(f"Hash length: {len(ADMIN_PASSWORD_HASH)}")
print(f"Hash starts with: {ADMIN_PASSWORD_HASH[:10]}")
print(
    f"Hash is valid bcrypt format: {ADMIN_PASSWORD_HASH.startswith(('$2a$', '$2b$', '$2y$'))}"
)
print("=" * 60)
