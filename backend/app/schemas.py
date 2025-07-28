from pydantic import BaseModel


class FibonacciResponse(BaseModel):
    result: int


class FactorialResponse(BaseModel):
    result: int


class PowResponse(BaseModel):
    result: float
