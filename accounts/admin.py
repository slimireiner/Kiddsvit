from django.contrib import admin
from django.contrib.admin import display

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'get_childrens']

    @display(description='Childrens')
    def get_childrens(self, obj):
        return [child.name for child in obj.childrens.all()]


class ChildrenAdmin(admin.ModelAdmin):
    pass


class AllScoreAdmin(admin.ModelAdmin):
    pass


class ShareTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Children, ChildrenAdmin)
admin.site.register(AllScore, AllScoreAdmin)
admin.site.register(ShareToken, ShareTokenAdmin)