from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from student.models import StudentModel
from student.serializers import studentSerializer
from student.services import get_all_students, insert_student, delete_student

# Create your views here.

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method=='GET':
        # studentvalue=StudentModel.objects.all()
        studentvalue=get_all_students()
        studentSerializerval=studentSerializer(studentvalue,many=True)
        return Response(studentSerializerval.data)

    elif request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            insert_student(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def student_delete_list(request,pk):
#     try:
#         studentDetails=StudentModel.objects.get(pk=pk)
#     except studentDetails.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     studentDetails.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def student_delete_list(request, pk):
    deleted = delete_student(pk)
    if deleted:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def student_update_list(request,pk):
    try:
        studentDetails=StudentModel.objects.get(pk=pk)
    except studentDetails.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)
    studentSerialize=studentSerializer(studentDetails,data=request.data)
    if studentSerialize.is_valid():
        studentSerialize.save()
        return Response(studentSerialize.data, status=status.HTTP_201_CREATED)
    return Response(studentSerialize.errors, status=status.HTTP_400_BAD_REQUEST)


