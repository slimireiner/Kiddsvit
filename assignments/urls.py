from django.urls import path
from . import views
from .views import ChildrenAddCourse

urlpatterns = [
path('add_course/', ChildrenAddCourse.as_view(), name='add_course'),
# path('update_task/', App.views.update_task, name='update_task'),
]