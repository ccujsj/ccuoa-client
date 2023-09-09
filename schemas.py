import datetime
from pydantic import BaseModel
from typing import Optional

class TextSchema(BaseModel):
    text_type:int
    text_key:str
    text_value:str


class StudentSchema(BaseModel):
    stu_id: str
    stu_name: str
    stu_score: float = 0.0
    stu_clazz: str
    stu_sex: Optional[str]
    stu_card: Optional[str]
    stu_nation: Optional[str]
    stu_politics: Optional[str]
    stu_origin: Optional[str]
    stu_home: Optional[str]
    stu_phone: Optional[str]
    stu_email: Optional[str]
    stu_location: Optional[str]
    stu_status: Optional[str]
    stu_graduate: Optional[str]

def student_filter_func(k,v):
    if k == "stu_id":
        v = str(v)
    if k == "stu_score":
        v = float(v)
    if k == "stu_clazz":
        v = str(v)
    if v is None:
        v = "missing"
    return v


class MoralRecordSchema(BaseModel):
    student_id: str
    student_name: str
    rec_types: str
    rec_score: float
    rec_urls: str
    rec_desc: str
    rec_date: datetime.datetime
    rec_msg: Optional[str]
    rec_status: int
    chk_username: str
    chk_commit: Optional[str]
    chk_date: datetime.datetime
def moral_filter_func(k,v):
    """
    filter function need to be redesigned after being deployed
    :param k: field name
    :param v: value of this field
    :return:
    """
    if k == "chk_date":
        v = datetime.datetime.now()
    if k == "rec_date":
        v = datetime.datetime.now()  # TODO this filter need to be changed
    if k == "rec_score":
        v = float(v)
    if k == "rec_status":
        v = int(v)
    if v is None:
        v = "missing"
    return v