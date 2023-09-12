from core.schemas import TextSchema
from core.session import ClintSession
session = ClintSession()
session.update_baseurl("http://localhost:8000")
session.set_bearer(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    ".eyJ1c3IiOiJhZG1pbiIsInNjb3BlIjpbInN0dWRlbnQiLCJzdGFmZiIsInN5c3RlbSJdLCJleHAiOjE2OTQzMzc3MzZ9"
    ".KWGThipWNm9e8sgC8BF-dSGP-C49EZ3F9Te7cnIR51U"
)

def upload_text(text_key:str,text_value:str,text_type:int=0):
    info = TextSchema(text_key=text_key,
                      text_value=text_value,
                      text_type=text_type)
    r = session.post("/api/v1/put/info/text",json=info.json())
    print(r)

upload_text('name','hello')
