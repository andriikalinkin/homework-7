from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=False)
    subject = models.CharField(max_length=255)


class Group(models.Model):
    name = models.CharField(max_length=255, null=False)
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
