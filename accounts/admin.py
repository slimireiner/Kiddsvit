from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    pass


class ChildrenAdmin(admin.ModelAdmin):
    pass


class AllScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Children, ChildrenAdmin)
admin.site.register(AllScore, AllScoreAdmin)