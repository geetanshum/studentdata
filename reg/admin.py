from django.contrib import admin
from .models import *
# Register your models here.

"""class StudentA(admin.ModelAdmin):
    model = Student
    list_display=['name','class','gender']"""


admin.site.register(Student)