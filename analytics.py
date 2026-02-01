from typing import Dict
from db import fetch_all


def category_summary() -> Dict[str, float]:
    rows = fetch_all("""
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
    """)
    return {row["category"]: row["total"] for row in rows}


def monthly_total(month: str) -> float:
    row = fetch_all("""
        SELECT SUM(amount) AS total
        FROM expenses
        WHERE strftime('%m', expense_date) = ?
    """, (month,))
    return row[0]["total"] or 0.0
