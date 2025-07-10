from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

### **1. List All Students (READ)**
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

### **2. Add New Student (CREATE)**
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

### **3. Update Student (UPDATE)**
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form})

### **4. Delete Student (DELETE)**
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete_student.html', {'student': student})