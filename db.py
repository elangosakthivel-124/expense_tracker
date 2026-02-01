import sqlite3
from contextlib import contextmanager
from typing import Iterable, Tuple

DB_NAME = "expenses.db"


@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def initialize_db() -> None:
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount > 0),
            description TEXT
        )
        """)


def execute(query: str, params: Tuple = ()) -> None:
    with get_connection() as conn:
        conn.execute(query, params)


def fetch_all(query: str, params: Tuple = ()) -> Iterable[sqlite3.Row]:
    with get_connection() as conn:
        return conn.execute(query, params).fetchall()
