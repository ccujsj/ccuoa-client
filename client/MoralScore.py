import datetime
from pydantic import BaseModel
from typing import Optional

from core.session import ClintSession


class MoralRecordSchema(BaseModel):
    student_id: str
    student_name: str
    rec_types: str
    rec_score: float
    rec_urls: str
    rec_desc: str
    rec_date: datetime.datetime
    rec_msg: Optional[str] = "无备注"
    rec_status: int
    chk_username: str
    chk_commit: Optional[str] = "无备注"
    chk_date: datetime.datetime

class MoralScore:
    def __init__(self,session:ClintSession):
        self.__s = session
        pass
    def upload_single_moral_record(self,record:MoralRecordSchema):
        pass
    def upload_batch_moral_record(self,records:list):
        pass
    def get_single_student_record(self,student_id):
        pass
