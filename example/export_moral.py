from core.schemas import StudentSchema
from core.session import ClintSession

session = ClintSession()
session.update_baseurl("http://localhost:8000")
session.set_bearer("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3IiOiJhZG1pbiIsInNjb3BlIjpbInN0dWRlbnQiLCJzdGFmZiIsInN5c3RlbSJdLCJleHAiOjE2OTQzMzc3MzZ9.KWGThipWNm9e8sgC8BF-dSGP-C49EZ3F9Te7cnIR51U")

def get_all_record():
    record_type = 4
    r = session.get(f"/api/v1/get/moral/record/byType?t={record_type}")
    d = r.json()
    for i in d:
        print(i)
def get_student_score(stu_id):
    l = session.get(f"/api/v1/get/student/info/id?stu_id={stu_id}")
    s = StudentSchema(**l.json())
    print(s.model_dump())

get_student_score("042040315")
get_all_record()
