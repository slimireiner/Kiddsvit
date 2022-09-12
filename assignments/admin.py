from django.contrib import admin

from assignments.models import Course, Progress, Task


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


class ProgressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Task, TaskAdmin)