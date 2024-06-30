from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveInt


class Email(BaseModel):
    id: Optional[PositiveInt]
    receiver_email: EmailStr
    subject: str
    body_text: str
