from django.db import models

# Create your models here.

class StudentModel(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Course=models.CharField(max_length=20)

