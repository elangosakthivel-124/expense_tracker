from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Expense:
    expense_date: date
    category: str
    amount: float
    description: str = ""
