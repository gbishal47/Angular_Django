# student/services.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Bishal"]
student_collection = db["student"]

def get_all_students():
    return list(student_collection.find({}, {'_id': 0}))

def insert_student(data):
    student_collection.insert_one(data)

def delete_student(studentId):
    result = student_collection.delete_one({"studentId": int(studentId)})
    return result.deleted_count > 0