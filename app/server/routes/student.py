"""
 As rotas para complementar as operações do banco de dados no arquivo de banco de dados.

"""

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.server.database import(
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)

from app.server.models.student import(
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()


@router.post('/', response_description='Student data added into the database')
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, 'Student added successfully.')
