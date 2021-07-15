from datetime import datetime

from typing import List, Optional

from pydantic import BaseModel



class ExtensionIn(BaseModel):
    Extension_Start_Number: int
    Extension_End_Number: int


class CallStartIn(BaseModel):
    Extension: int
    TargetNumber: str


class CallStopIn(BaseModel):
    TargetNumber: str


class UserTextIn(BaseModel):
    Text: str
    TargetNumber: str


class BotTextIn(BaseModel):
    Extension: int
    Text: str

class BotOut(BaseModel):
    code: str
    extension: str
    createdAt: str
    phoneNumber: str
    status: str

class TextOut(BaseModel):
    createdAt: str
    userText: str = None
    botText: str = None

class OutBoutIn(BaseModel):
    username: str
    usecall: str