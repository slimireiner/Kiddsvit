from django import forms
from django.contrib import admin

from assignments.models import Course, TaskProgress, Task, ChildrenCourseRelation
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    pass


class TaskAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task
        fields = '__all__'


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'score', 'course', 'content']
    form = TaskAdminForm


class TaskProgressAdmin(admin.ModelAdmin):
    list_display = ['children', 'task', 'task_status', 'created_ad', 'finished_ad']


class ChildrenCourseRelationAdmin(admin.ModelAdmin):
    list_display = ['children', 'course', 'created_ad', 'finished_ad']


admin.site.register(Course, CourseAdmin)
admin.site.register(TaskProgress, TaskProgressAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(ChildrenCourseRelation, ChildrenCourseRelationAdmin)