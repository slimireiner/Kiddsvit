from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.assign_course, name='add_course'),
    path('start_task/', views.start_task, name='start_task'),
    path('add_score_end_task/', views.add_score_end_task, name='add_score_end_task'),
]