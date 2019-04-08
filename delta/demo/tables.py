import django_tables2 as tables
from .models import *

class SectionAssignmentsTable(tables.Table):
    class Meta:
        model = Assignment
        template_name = 'django_tables2/semantic.html'

class StudentDetailTable(tables.Table):
    class Meta:
        model = Student
        template_name = 'django_tables2/semantic.html'
