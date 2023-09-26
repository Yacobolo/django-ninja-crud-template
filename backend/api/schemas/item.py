# schemas.py
from datetime import datetime
from typing import Optional

from ninja import Schema


class ItemIn(Schema):
    name: str
    description: Optional[str] = None


class ItemOut(Schema):
    id: int
    name: str
    description: Optional[str]
    created_at: datetime
    created_by_id: Optional[int]
    updated_at: datetime
    updated_by_id: Optional[int]
    is_active: bool
