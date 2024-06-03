import fastapi
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@router.get("/users", response_model=List[User])
async def get_user():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return users

@router.get("/user/{id}")
async def get_user(id: int):
    return { "user": users[id]}