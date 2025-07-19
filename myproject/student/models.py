from django.db import models
from db_connection import db

# Create your models here.

person_collection=db['student']

class StudentModel(models.Model):
    Id = models.AutoField(primary_key=True)
    studentId = models.IntegerField(default=0)
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Course = models.CharField(max_length=60)

    def save(self, *args, **kwargs):
        # Save to SQLite first
        super().save(*args, **kwargs)

        # Sync to MongoDB
        person_collection.update_one(
            {"Id": self.Id},
            {
                "$set": {
                    "Id": self.Id,
                    "Name": self.Name,
                    "Age": self.Age,
                    "Course": self.Course
                }
            },
            upsert=True
        )

