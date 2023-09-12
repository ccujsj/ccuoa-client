from core.mapping_model import load_excel_to_model
from core.schemas import StudentSchema, student_filter_func
from core.session import ClintSession

li = load_excel_to_model("student_datasource.xlsx", StudentSchema, student_filter_func)
session = ClintSession()
session.set_bearer("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3IiOiJ6aGFuZ3poZW5nIiwic2NvcGUiOlsic3R1ZGVudCIsInN0YWZmIiwic3lzdGVtIl0sImV4cCI6MTY5NDQyNzU5N30.7J3_Nj_QlSzBSOqbUy0LwtVN5ndhPm7iILv1CZtj14M")
for student in li:
    r = session.post("/api/v1/put/student/info",json=student.model_dump(mode='json'))
    print(r)
