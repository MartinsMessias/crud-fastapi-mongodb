"""
No código abaixo, importamos Motor, definimos os detalhes da conexão e criamos um cliente via AsyncIOMotorClient .
Em seguida, referenciamos um banco de dados chamado students e uma coleção chamada students_collection. Visto que são apenas referências e não E/S reais, nenhum deles requer uma expressão await. Quando a primeira operação de I/O for feita, o banco de dados e a coleção serão criados, se ainda não existirem.
Em seguida, uma função auxiliar rápida para analisar os resultados de uma consulta ao banco de dados em um dicionário Python.
"""
import os

import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

try:
    MONGO_DETAILS = config('MONGO_DETAILS')
except:
    MONGO_DETAILS = os.getenv('MONGO_DETAILS')

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


# Trazer todos os alunos presentes no banco de dados
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Adicionar um novo estudante no banco de dados
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Trazer um estudante passando seu ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({'_id': ObjectId(id)})
    if student:
        return student_helper(student)


# Atualizar um estudante passando seu ID
async def update_student(id: str, data: dict):
    # Retorna falso se o body for vazio
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False

# Deletar um estudante


async def delete_student(id: str):
    student = await student_collection.find_one({'_id': ObjectId(id)})
    if student:
        await student_collection.delete_one({'_id': ObjectId(id)})
        return True
