from rest_framework import serializers;
from student.models import StudentModel
from db_connection import db

person_collection=db['student']
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__'

