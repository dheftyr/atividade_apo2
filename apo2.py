
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "escola.db"


def conectar() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
