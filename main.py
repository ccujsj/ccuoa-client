"""
example for usage
"""
from client.StudentInfo import StudentInfo,StudentSchema
from client.MoralScore import MoralRecordSchema,MoralScore
from client.InfoText import TextSchema,InfoText
from core.env_load import load
from core.excel_mapping import ExcelModel
from core.session import ClientSession
from debug import test_construct
import os

os.environ.update(load(".env"))

session = ClientSession()
session.show_send(True)
session.login(os.environ.get("username"),os.environ.get("password"))

# session.set_bearer()  # set_bearer is available if you have a bearer from admin-web
student_network_client = StudentInfo(session)
info_text_client = InfoText(session)
moral_client = MoralScore(session)
de = {}
for d in test_construct:
    de.update(d)
excel = ExcelModel("moral_text_sheet.xlsx")
ret = excel.instantiation(de,MoralRecordSchema)
moral_client.upload_batch_moral_record(ret)

student_network_client.upload_single_student_info(StudentSchema(stu_id="042040000",stu_name="zhangsan",stu_score=0.0,stu_clazz="20400"))