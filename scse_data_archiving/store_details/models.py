import datetime


from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import validate_email

from model_utils.models import TimeStampedModel
from model_utils import Choices
import reversion
from stdimage import StdImageField

joining_year_choices = []
for year in range(2000, (datetime.datetime.now().year + 1)):
    joining_year_choices.append(year)


class Faculty(TimeStampedModel):
    _registry = []
    faculty_code = models.CharField(max_length=255)
    image = StdImageField(upload_to='faculty_images/', null=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.date.today)
    age = models.IntegerField()
    current_subjects = models.CharField(max_length=255)
    research_interest = models.CharField(max_length=255, blank=True)
    joining_year = models.CharField(
        max_length=5,)
    projects = models.CharField(max_length=255, blank=True)
    email = models.EmailField(
        max_length=254, null=True, unique=True, validators=[validate_email, ])
    address = models.TextField(max_length=200)
    mobile_number = models.IntegerField()
    land_line = models.IntegerField()


class Student(TimeStampedModel):
    _registry = []
    entry_number = models.CharField(max_length=255)
    image = StdImageField(upload_to='student_images/', null=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.date.today)
    age = models.IntegerField()
    current_semester = models.IntegerField()
    joining_year = models.CharField(
        max_length=5, )
    projects = models.CharField(max_length=255, blank=True)
    email = models.EmailField(
        max_length=254, null=True, unique=True, validators=[validate_email, ])
    address = models.TextField(max_length=200)
    mobile_number = models.IntegerField()
    land_line = models.IntegerField()


class OtherStaff(TimeStampedModel):
    _registry = []
    image = StdImageField(upload_to='otherstaff_images/', null=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.date.today)
    age = models.IntegerField()
    joining_year = models.CharField(
        max_length=5, )
    email = models.EmailField(
        max_length=254, null=True, unique=True, validators=[validate_email, ])
    address = models.TextField(max_length=200)
    mobile_number = models.IntegerField()
    land_line = models.IntegerField()
