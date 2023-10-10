from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField(null=False)
    subject = models.CharField(max_length=255)


class Group(models.Model):
    name = models.CharField(max_length=255)
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
