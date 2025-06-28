from rest_framework import serializers;
from student.models import StudentModel
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__'

