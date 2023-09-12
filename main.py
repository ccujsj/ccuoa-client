"""
example for usage
"""
from client.StudentInfo import StudentInfo,StudentSchema
from core.env_load import load
import os
from core.session import ClintSession
os.environ.update(load(".env"))

session = ClintSession()
session.show_send(True)
session.login(os.environ.get("username"),os.environ.get("password"))

# session.set_bearer()  # set_bearer is available if you have a bearer from admin-web

student_network_client = StudentInfo(session)

student_network_client.upload_single_student_info(StudentSchema(stu_id="042040000",stu_name="zhangsan",stu_score=0.0,stu_clazz="20400"))
