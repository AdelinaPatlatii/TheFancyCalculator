from pydantic import BaseModel


class FibonacciResponse(BaseModel):
    result: int


class FactorialResponse(BaseModel):
    result: int


class PowResponse(BaseModel):
    result: float


class GCDResponse(BaseModel):
    result: int


class LCMResponse(BaseModel):
    result: int


class LogResponse(BaseModel):
    result: float


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
