from core.mapping_model import load_excel_to_model
from core.schemas import MoralRecordSchema, moral_filter_func
from core.session import ClintSession

li = load_excel_to_model("moral.xlsx", MoralRecordSchema, moral_filter_func)
session = ClintSession()

session.set_bearer("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3IiOiJhZG1pbiIsInNjb3BlIjpbInN0dWRlbnQiLCJzdGFmZiIsInN5c3RlbSJdLCJleHAiOjE2OTQzMzc3MzZ9.KWGThipWNm9e8sgC8BF-dSGP-C49EZ3F9Te7cnIR51U")
for student in li:
    r = session.post("/api/v1/new/record/withResult",json=student.model_dump(mode='json'))
    pass

session.get("/api/v1/update/moral/publish")

