

import datetime
from pydantic import BaseModel
from typing import Optional

from core.session import ClientSession


class TextSchema(BaseModel):
    text_type:int
    text_key:str
    text_value:str

def TextSchema_filter(field:str,value:str):
    if field == "text_type":
        if value is None:
            return 0
        return int(value)


class InfoText:
    def __init__(self,session:ClientSession):
        self.__s = session
        pass
    def create_text(self,text:TextSchema):
        r = self.__s.post("/api/v1/put/info/text",date=text.json())
        return r
        pass
    def update_text(self,text:TextSchema):
        r = self.__s.get(f"/api/v1/delete/info/byKey?key={text.text_key}")
        if r.status_code == 200:
            ir = self.create_text(text)
            print(f"text with key {text.text_key} upload success")
            return ir
        pass
    def retrieve_text_by_name(self,name):
        r = self.__s.get("/api/v1/get/info/all")
        for i in r.json():
            if i.text_key == name:
                return i

        pass
    def retrieve_text_all(self):
        r = self.__s.get("/api/v1/get/info/all")
        return r.json()
        pass
    def delete_text_by_name(self,name):
        r = self.__s.get(f"/api/v1/delete/info/byKey?key={name}")
        if r.status_code == 200:
            print("delete success")
        pass