
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

def inserir_dados_iniciais(conn: sqlite3.Connection) -> None:
    with conn:
        conn.executemany(
            "INSERT INTO cursos (nome, carga_horaria) VALUES (?, ?);",
            [
                ("Análise e Desenvolvimento de Sistemas", 2400),
                ("Redes de Computadores", 2000),
            ],
        )
        conn.executemany(
            "INSERT INTO estudantes (nome, email, id_curso) VALUES (?, ?, ?);",
            [
                ("Ana Silva", "ana.silva@exemplo.edu.br", 1),
                ("Bruno Costa", "bruno.costa@exemplo.edu.br", 1),
                ("Carla Souza", "carla.souza@exemplo.edu.br", 2),
            ],
        )

def consultar_join(conn: sqlite3.Connection, titulo: str) -> None:
    print(f"\n--- {titulo} ---")
    cursor = conn.execute("""
        SELECT
            e.id_estudante,
            e.nome AS estudante,
            e.email,
            c.nome AS curso,
            c.carga_horaria
        FROM estudantes e
        INNER JOIN cursos c ON e.id_curso = c.id_curso
        ORDER BY e.id_estudante;
    """)
    for linha in cursor.fetchall():
        print(linha)
