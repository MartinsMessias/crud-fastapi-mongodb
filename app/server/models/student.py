"""
No código abaixo, definimos um esquema Pydantic chamado StudentSchema que representa como os dados do aluno serão armazenados em seu banco de dados MongoDB.

Em Pydantic, o reticências , ..., indica que um campo é obrigatório. Ele pode ser substituído por None ou um valor padrão. Em StudentSchema, cada campo possui reticências, pois cada campo é importante e o programa não deve prosseguir sem ter os valores configurados.

No campo gpa e year no StudentSchema, nós adicionamos os validadores 'gt', 'lt' e 'le':

'gt' e 'lt'  no campo year garante que o valor passado seja maior que 0 e menor que 9 . Como resultado, valores como 0 , 10 , 11 resultarão em erros.
validador 'le' no campo  gpa garante que o valor passado seja menor ou igual a 4,0 .
Esse esquema ajudará os usuários a enviar solicitações HTTP com a forma adequada para a API - por exemplo, o tipo de dados a enviar e como enviá-los.
"""
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'John Doe',
                'email': 'jdoe@x.edu.ng',
                'course_of_study': 'Water resourses engineering',
                'year': 2,
                'gpa': '3.9'
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[str]
    course_of_study: Optional[str]
    year: Optional[str]
    gpa: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'John Doe',
                'email': 'jdoe@x.edu.ng',
                'course_of_study': 'Water resourses engineering',
                'year': 4,
                'gpa': '4.0'
            }
        }


def ResponseModel(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message
    }


def ErrorResponseModel(error, code, message):
    return {'error': error, 'code': code, 'message': message}
