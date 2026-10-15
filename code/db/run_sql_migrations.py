from __future__ import annotations

import os
from pathlib import Path

import pymysql

ROOT = Path(__file__).resolve().parents[1]
DOTENV_PATH = ROOT / ".env"
SQL_DIR = ROOT / "db" / "sql"


def load_dotenv() -> None:
    if not DOTENV_PATH.exists():
        return

    for line in DOTENV_PATH.read_text().splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#") or "=" not in raw:
            continue
        key, value = raw.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def split_statements(sql_text: str) -> list[str]:
    return [stmt.strip() for stmt in sql_text.split(";") if stmt.strip()]


def main() -> None:
    load_dotenv()

    conn = pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "interview_user"),
        password=os.getenv("DB_PASSWORD", "interview_pass"),
        database=os.getenv("DB_NAME", "interview_db"),
        autocommit=False,
    )

    try:
        files = sorted(SQL_DIR.glob("*.sql"))
        with conn.cursor() as cursor:
            for sql_file in files:
                sql_text = sql_file.read_text()
                for statement in split_statements(sql_text):
                    cursor.execute(statement)
                conn.commit()
                print(f"Applied {sql_file.name}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
