"""
No código abaixo, importamos Motor, definimos os detalhes da conexão e criamos um cliente via AsyncIOMotorClient .
Em seguida, referenciamos um banco de dados chamado students e uma coleção chamada students_collection. Visto que são apenas referências e não E/S reais, nenhum deles requer uma expressão await. Quando a primeira operação de I/O for feita, o banco de dados e a coleção serão criados, se ainda não existirem.
Em seguida, uma função auxiliar rápida para analisar os resultados de uma consulta ao banco de dados em um dicionário Python.
"""

import motor.motor_asyncio

MONGO_DETAILS = 'mongodb+srv://userhere:passwordhere@projectx.saeyn.mongodb.net/projectx?retryWrites=true&w=majority'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection('students_collection')

# helpers


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }
