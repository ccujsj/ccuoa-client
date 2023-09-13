from core.session import ClientSession
import datetime
from pydantic import BaseModel
from typing import Optional,List


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

def StudentSchema_filter(field:str,value:str):
    if field == "stu_score":
        if value is None:
            return 0.0
        return float(value)

class StudentInfo:
    def __init__(self,session:ClientSession):
        self.__s = session
        pass

    def upload_single_student_info(self,student:StudentSchema):
        r = self.__s.post("/api/v1/put/student/info",json=student.dict())
        print(r)
    def upload_batch_student_info(self,students:List[StudentSchema]):
        success_list = []
        failed_list = []
        for student in students:
            r = self.__s.post("/api/v1/put/student/info", json=student.dict())
            if r.status_code == 200:
                success_list.append(student.stu_id)
            else:
                failed_list.append(student.stu_id)
        print(f"{len(success_list)} upload succeeded, {len(failed_list)} upload failed")
        pass
    def get_single_student_info(self,student_id):
        r = self.__s.get("/api/v1/get/student/info/id?stu_id=" + student_id)
        if r.status_code == 200:
            return r.json()  # TODO Dump to student Schema
        pass
    def get_students_info(self):
        # todo sqlalchemy are needed to access mysql database directly.
        pass

