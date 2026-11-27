
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "escola.db"


def conectar() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def criar_tabelas(conn: sqlite3.Connection) -> None:
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cursos (
                id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                carga_horaria INTEGER NOT NULL
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS estudantes (
                id_estudante INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                id_curso INTEGER NOT NULL,
                FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
            );
        """)