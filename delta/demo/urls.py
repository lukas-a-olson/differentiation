from django.urls import path

from . import views

urlpatterns = [
               # ex: /demo/
               path('', views.index, name='index'),
               # ex: /demo/student/1/
               path('student/<int:student_id>/', views.student_detail, name='student_detail'),
               # /demo/section-1/assignments/
               path('section-<int:section_id>/assignments/', views.section_assignments, name='gradebook'),
               ]
