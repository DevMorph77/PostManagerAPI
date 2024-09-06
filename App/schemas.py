from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int

    class Config:
        orm_mode = True
