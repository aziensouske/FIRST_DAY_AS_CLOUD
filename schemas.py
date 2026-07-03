from pydantic import BaseModel


# Register User Schema
class UserCreate(BaseModel):
    name: str
    email: str
    password: str


# Login User Schema
class UserLogin(BaseModel):
    email: str
    password: str


# Create Note Schema
class NoteCreate(BaseModel):
    title: str
    content: str


# Response Schema for Notes
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    class Config:
        from_attributes = True

