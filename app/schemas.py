from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class FieldMetadata(BaseModel):
    max_length: Optional[int] = None
    min_length: Optional[int] = None
    pattern: Optional[str] = None
    styles: Dict[str, Any]
    action: Optional[str] = None
    min: Optional[int] = None
    max: Optional[int] = None
    allow_other: Optional[bool] = False


class Field(BaseModel):
    id: str
    name: str
    type: str
    required: bool
    placeholder: Optional[str] = None
    options: Optional[List[str]] = None
    metadata: FieldMetadata


class Page(BaseModel):
    name: str
    fields: List[Field]


class FormConfig(BaseModel):
    name: str
    description: str
    creator: str
    version: str
    page_count: int
    form_timeout: int
    pages: List[Page]


class FormBase(BaseModel):
    name: str
    description: str
    creator: str
    version: str
    page_count: int
    form_timeout: int
    pages: List[Page]


class FormCreate(FormBase):
    pass


class Form(FormBase):
    id: str
    is_active: bool

    class Config:
        orm_mode = True


class FormListResponse(BaseModel):
    data: List[Form]


class FormActivateDeactivate(BaseModel):
    activate: bool


class SubmissionBase(BaseModel):
    form_id: str
    data: dict


class SubmissionCreate(SubmissionBase):
    pass


class Submission(SubmissionBase):
    id: int

    class Config:
        orm_mode = True
