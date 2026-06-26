from pathlib import Path
import os

from dotenv import load_dotenv


def load_openai_api_key() -> str:
    project_root = Path(__file__).resolve().parent
    env_path = project_root / ".env"

    if not env_path.exists():
        raise FileNotFoundError(f".env file not found at {env_path}")

    load_dotenv(env_path)
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(f"OPENAI_API_KEY is missing in {env_path}")

    os.environ["OPENAI_API_KEY"] = api_key
    return api_key


def main():
    load_openai_api_key()
    print("OPENAI_API_KEY loaded successfully.")


if __name__ == "__main__":
    main()
