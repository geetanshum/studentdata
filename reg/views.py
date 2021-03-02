from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from .models import Student
# Create your views here.

#creating and retrieving the data
class StudentView(CreateView,ListView):
    model = Student
    fields = ['name','email','gender']
    template_name ="index.html"
    success_url = '/'
    stu = Student.objects.all()
    context_object_name = 'stu'

#updating the data
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','gender']
    template_name ='updateForm.html'
    success_url = '/'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'deleteForm.html'
    success_url = '/'