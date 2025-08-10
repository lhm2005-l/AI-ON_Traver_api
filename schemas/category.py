# 데이터 타입을 정의
from pydantic import BaseModel, Field

class Icategory(BaseModel):
    # key값
    alone: bool = Field(...)        # ...은 NULL 값은 허용하지 않음
    friend: bool = Field(...)
    lover: bool = Field(...)
    family: bool = Field(...)

    # value 값
    experience: bool = Field(...)
    sns: bool = Field(...)
    nature: bool = Field(...)
    famous: bool = Field(...)
    healing: bool = Field(...)
    culture: bool = Field(...)
    shopping: bool = Field(...)