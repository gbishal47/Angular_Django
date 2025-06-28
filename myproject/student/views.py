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

    elif request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

