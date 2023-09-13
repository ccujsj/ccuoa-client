import datetime
import string

from pydantic import BaseModel
from typing import Optional,List

from core.session import ClientSession


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

def tencent_doc_date(date_string:str):
    """
    input a date_string like 2023年6月5日
    Public module string in python has a `printable` which only contains english letter
    use the true/false flip to create a virtual stack
    :param date_string: string
    :return:
    """
    date = []
    date_meta = ""
    for c in date_string:
        if c in string.printable:
            date_meta += c
        else:
            date.append(int(date_meta))
            date_meta = ""
    return datetime.datetime(date[0], date[1], date[2], 12, 0, 0)



def MoralRecordSchema_filter(field:str,value:str):
    print({field:value})
    if field == "rec_score":
        if value is None:
            return 0.0
        return float(value)
    if field == "rec_date":
        return tencent_doc_date(value)
    if field == "rec_status":
        if value is None:
            return 0
        return int(value)
    if field == "chk_date":
        return tencent_doc_date(value)
    if field == 'chk_username':
        if value is None:
            return "anonymous"
    return value


class MoralScore:
    def __init__(self,session:ClientSession):
        self.__s = session
        pass
    def upload_single_moral_record(self,record:MoralRecordSchema):
        pass
    def upload_batch_moral_record(self,records:List[MoralRecordSchema]):
        success_list = []
        failed_list = []
        for record in records:
            r = self.__s.post("/api/v1/new/record/withResult",data=record.json())
            if r.status_code == 200:
                success_list.append(record.student_name)
            else:
                failed_list.append(record.student_name)
        print(f"{len(success_list)} upload succeeded, {len(failed_list)} upload failed")
        pass
    def get_single_student_record(self,student_id):
        pass





