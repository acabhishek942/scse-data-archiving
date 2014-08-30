from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic.detail import DetailView

from .models import Faculty, Student, OtherStaff


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
