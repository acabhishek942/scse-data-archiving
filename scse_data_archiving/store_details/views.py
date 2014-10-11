from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic.detail import DetailView

from .models import Faculty, Student, OtherStaff
from .forms import StudentForm


class FacultyDetail(DetailView):
    model = Faculty
    slug_field = 'faculty_code'


class StudentDetail(DetailView):
    model = Student
    slug_field = 'entry_number'


def home(request):
    return render(request, 'home.html', {})


class OtherStaffDetail(DetailView):
    model = OtherStaff
    slug_field = 'code'


def new_student(request):
    template_name = 'store_details/new_student.html'
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return HttpResponseRedirect(reverse('home', args=()))
    else:
        form = StudentForm()
        return render(request, template_name, {'form': form, })
