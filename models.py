from sqlalchemy import Column, BigInteger, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.functions import now

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, server_default=now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    verified = Column(Boolean, default=False, nullable=False)
