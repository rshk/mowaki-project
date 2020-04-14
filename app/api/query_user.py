from typing import List

from app.core.user import UsersCore

from .base import schema
from .user import User


@schema.query.field('users')
def query_users(root, info) -> List[User]:
    users = UsersCore.from_request().list()
    return list(users)


@schema.query.field('user')
def query_user(root, info, id: int) -> User:
    return UsersCore.from_request().get(id)
