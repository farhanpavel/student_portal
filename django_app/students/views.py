from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm  # You'll need to create this form

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_list')