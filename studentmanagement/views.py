from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .forms import StudentForm
from .models import Student
# Create your views here.

# class based view

class StudentRecordFormView(FormView):
    template_name = 'book_form.html'
    form_class = StudentForm
    success_url = '/student_management/entry_success'

    def form_valid(self, form):
        form.save()
        # call the base class so that it would redirect to success_url after successful validation
        return super(StudentRecordFormView, self).form_valid(form)

class FormSuccessView(View):
    def get(self, request , *args, **kwargs):
        return HttpResponse('Student Saved Successfully')

# CRUD with class based view

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'hobby']
    template_name = 'book_form.html'
    success_url = '/student_management/entry_success'

class StudentRecordDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

class StudentRecordUpdate(UpdateView):
    model = Student
    fields = ['name', 'hobby']
    template_name = 'book_form.html'
    success_url = '/student_management/entry_success'

class StudentRecordDelete(DeleteView):
    model = Student
    template_name = 'book_form.html'
    success_url = '/student_management/entry_success'