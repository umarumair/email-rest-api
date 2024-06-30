from typing import Optional, ClassVar

from pydantic import BaseModel, EmailStr, Field


class Email(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: Email._increment_id())
    receiver_email: EmailStr
    subject: str
    body_text: str

    _current_id: ClassVar[int] = 0

    @classmethod
    def _increment_id(cls) -> int:
        cls._current_id += 1
        return cls._current_id
