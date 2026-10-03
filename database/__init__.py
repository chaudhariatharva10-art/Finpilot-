"""Database package for future persistence-related code."""

from .connection import placeholder as connection_placeholder
from .profiles import placeholder as profiles_placeholder
from .income import placeholder as income_placeholder
from .expenses import placeholder as expenses_placeholder
from .loans import placeholder as loans_placeholder
from .goals import placeholder as goals_placeholder
from .history import placeholder as history_placeholder

__all__ = [
    "connection_placeholder",
    "profiles_placeholder",
    "income_placeholder",
    "expenses_placeholder",
    "loans_placeholder",
    "goals_placeholder",
    "history_placeholder",
]
