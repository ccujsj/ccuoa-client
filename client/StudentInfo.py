from core.session import ClintSession
import datetime
from pydantic import BaseModel
from typing import Optional


class StudentSchema(BaseModel):
    stu_id: str
    stu_name: str
    stu_score: float = 0.0
    stu_clazz: str
    stu_sex: Optional[str] = "未知"
    stu_card: Optional[str] = "未知"
    stu_nation: Optional[str] = "未知"
    stu_politics: Optional[str] = "未知"
    stu_origin: Optional[str] = "未知"
    stu_home: Optional[str] = "未知"
    stu_phone: Optional[str] = "未知"
    stu_email: Optional[str] = "未知"
    stu_location: Optional[str] = "未知"
    stu_status: Optional[str] = "未知"
    stu_graduate: Optional[str] = "未知"

class StudentInfo:
    def __init__(self,session:ClintSession):
        self.__s = session
        pass

    def upload_single_student_info(self,student:StudentSchema):
        r = self.__s.post("/api/v1/put/student/info",json=student.dict())
        print(r)
    def upload_batch_student_info(self,students:list):
        pass
    def get_single_student_info(self,student_id):
        pass
    def get_students_info(self):
        pass

