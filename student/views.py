

from multiprocessing import context
from django.shortcuts import render

from .forms import StudentForm

def index(request):
    return render(request, 'student/index.html')

# def student_page(request):
#     return render(request,'student/student.html')

def student_page(request):
    form = StudentForm()
    context = {
        'form' : form
    }

    return render(request, 'student/student.html', context)