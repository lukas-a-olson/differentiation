from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig

from .models import *
from .tables import *


def index(request):
    return HttpResponse("Hello, world. You're at the demo index.")

def student_detail(request, student_id):
    table = StudentDetailTable(Student.objects.filter(student_id=student_id))
    RequestConfig(request).configure(table)
    params = {
        'title': 'Student Detail',
        'description': 'Student Detail',
        'table': table
    }
    return render(request, 'demo/simple_table.html', params)

def section_assignments(request, section_id):
    table = SectionAssignmentsTable(Assignment.objects.filter(section=section_id))
    RequestConfig(request).configure(table)
    params = {
        'title': 'Assignments',
        'description': f'Assignments for Section {section_id}',
        'table': table
    }
    return render(request, 'demo/simple_table.html', params)
