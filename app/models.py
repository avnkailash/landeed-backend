from sqlalchemy import Column, Integer, String, Boolean, JSON
from .db import Base


class Form(Base):
    __tablename__ = "forms"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    creator = Column(String)
    version = Column(String)
    page_count = Column(Integer)
    form_timeout = Column(Integer)
    pages = Column(JSON)
    is_active = Column(Boolean, default=True)


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(String, index=True)
    data = Column(JSON)
