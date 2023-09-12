import datetime
from pydantic import BaseModel
from typing import Optional

from core.session import ClintSession


class TextSchema(BaseModel):
    text_type:int
    text_key:str
    text_value:str

class InfoText:
    def __init__(self,session:ClintSession):
        self.__s = session
        pass
    def create_text(self,text:TextSchema):
        pass
    def update_text(self,text:TextSchema):
        pass
    def retrieve_text_by_name(self,name):
        pass
    def retrieve_text_all(self):
        pass
    def delete_text_by_name(self,name):
        pass