from django.db import models

# Create your models here.
class Student(models.Model):
    gende = (
        ('M','male'),
        ('F','female')
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1,choices=gende)

    def __str__(self):
        return self.name