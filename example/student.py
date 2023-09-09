from mapping_model import load_excel_to_model
from schemas import StudentSchema, student_filter_func
from session import ClintSession

li = load_excel_to_model("student_datasource.xlsx", StudentSchema, student_filter_func)
session = ClintSession()
session.update_baseurl("http://localhost:8000")
session.set_bearer("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3IiOiJhZG1pbiIsInNjb3BlIjpbInN0dWRlbnQiLCJzdGFmZiIsInN5c3RlbSJdLCJleHAiOjE2OTQzMzc3MzZ9.KWGThipWNm9e8sgC8BF-dSGP-C49EZ3F9Te7cnIR51U")
for student in li:
    r = session.post("/api/v1/put/student/info",json=student.model_dump(mode='json'))
    print(r)