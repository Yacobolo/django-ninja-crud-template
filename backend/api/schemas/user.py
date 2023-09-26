from ninja import Schema


class UserIn(Schema):
    username: str
    email: str
    password: str


class UserOut(Schema):
    id: int
    username: str
    email: str
