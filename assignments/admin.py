from django.contrib import admin

from assignments.models import Course, TaskProgress, Task


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


class TaskProgressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(TaskProgress, TaskProgressAdmin)
admin.site.register(Task, TaskAdmin)