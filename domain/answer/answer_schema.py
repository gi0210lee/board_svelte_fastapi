from datetime import datetime
from pydantic import BaseModel, validator
from domain.user.user_schema import User


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    @classmethod
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다')
        return v


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime
    user: User | None
    question_id: int
    modify_date: datetime | None = None
    voter: list[User] = []

    class Config:
        from_attributes = True


class AnswerUpdate(AnswerCreate):
    answer_id: int


class AnswerDelete(BaseModel):
    answer_id: int


class AnswerVote(BaseModel):
    answer_id: int