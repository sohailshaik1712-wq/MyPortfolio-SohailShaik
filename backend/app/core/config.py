import os

from app.core.security import verify_password
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

print(verify_password("moundlitch21", ADMIN_PASSWORD_HASH))

# Optional
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
