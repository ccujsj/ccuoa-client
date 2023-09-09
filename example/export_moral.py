from mapping_model import load_excel_to_model
from session import ClintSession

session = ClintSession()
session.update_baseurl("http://localhost:8000")
session.set_bearer("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3IiOiJhZG1pbiIsInNjb3BlIjpbInN0dWRlbnQiLCJzdGFmZiIsInN5c3RlbSJdLCJleHAiOjE2OTQzMzc3MzZ9.KWGThipWNm9e8sgC8BF-dSGP-C49EZ3F9Te7cnIR51U")
record_type = 4
r = session.get(f"/api/v1/get/moral/record/byType?t={record_type}")
print(r.json())