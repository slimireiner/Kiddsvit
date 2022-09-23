from django.contrib import admin

from assignments.models import Course, TaskProgress, Task, ChildrenCourseRelation


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'score', 'course']


class TaskProgressAdmin(admin.ModelAdmin):
    list_display = ['children', 'task', 'task_status', 'created_ad', 'finished_ad']


class ChildrenCourseRelationAdmin(admin.ModelAdmin):
    list_display = ['children', 'course', 'created_ad', 'finished_ad']


admin.site.register(Course, CourseAdmin)
admin.site.register(TaskProgress, TaskProgressAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(ChildrenCourseRelation, ChildrenCourseRelationAdmin)