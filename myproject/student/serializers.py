from rest_framework import serializers;
from student.models import StudentModel
class studentSerializer(serializers.modelSerializer):
    class Meta:
        models=StudentModel
        fields='__all__'

