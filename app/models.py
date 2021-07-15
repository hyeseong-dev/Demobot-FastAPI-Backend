from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey,
    Table
    )

from sqlalchemy.orm import Session, relationship
from sqlalchemy.sql.sqltypes import INTEGER
from app.database import Base


class Codes(Base):
    __tablename__ = 'codes'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, default=200)
    bots = relationship('Bots', back_populates='codes')


class Bots(Base):
    __tablename__ = 'bots'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean, default=False)
    extension = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    code_id = Column(Integer, ForeignKey('codes.id'), nullable=False)
    codes = relationship('Codes', back_populates='bots')
    users = relationship('Users', secondary='user_bots')


class BotText(Base):
    __tablename__ = 'bot_texts'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, default='', nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    bot_text_id = Column(Integer, ForeignKey('codes.id'), nullable=False)
    bots = relationship('Bots', back_populates='bot_texts')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    bots = relationship('Bots', secondary='user_bots')

class UserTexts(Base):
    __tablename__ = 'user_texts'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, default='', nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    users = relationship('Users', back_populates='user_texts')


class UserBots(Base):
    __tablename__ = 'user_bots'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    bot_id = Column(Integer, ForeignKey('bots.id'), primary_key=True)