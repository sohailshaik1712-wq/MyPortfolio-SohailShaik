import os

from dotenv import load_dotenv

load_dotenv()


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")

    if name == "ADMIN_PASSWORD_HASH":
        value = value.strip()
        # Handle cases where the hash might be wrapped in b'' strings
        if (value.startswith("b'") and value.endswith("'")) or (
            value.startswith('b"') and value.endswith('"')
        ):
            value = value[2:-1]

    return value


# --- Required Config ---
ADMIN_USERNAME: str = _require_env("ADMIN_USERNAME")
ADMIN_PASSWORD_HASH: str = _require_env("ADMIN_PASSWORD_HASH")
SECRET_KEY: str = _require_env("SECRET_KEY")

# --- New Integrations ---
DATABASE_URL: str = _require_env("DATABASE_URL")
GEMINI_API_KEY: str = _require_env("GEMINI_API_KEY")
PUSHOVER_USER: str = _require_env("PUSHOVER_USER")
PUSHOVER_TOKEN: str = _require_env("PUSHOVER_TOKEN")

# --- Default Settings ---
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

# --- DEBUG INFO ---
print("=" * 60)
print("CONFIG DEBUG INFO (SANITIZED):")
print(f"Username: {ADMIN_USERNAME}")
print(
    f"Database Host: {DATABASE_URL.split('@')[-1].split('/')[0]}"
)  # Only shows the host
print(f"Hash starts with: {ADMIN_PASSWORD_HASH[:10]}")
print(
    f"Is valid hash format: {ADMIN_PASSWORD_HASH.startswith(('$2a$', '$2b$', '$2y$'))}"
)
print("=" * 60)
