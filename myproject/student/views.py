from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from student.models import StudentModel
from student.serializers import studentSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method=='GET':
        studentvalue=StudentModel.objects.all()
        studentSerializerval=studentSerializer(studentvalue,many=True)
        return Response(studentSerializerval.data)

