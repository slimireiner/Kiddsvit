from django.contrib import admin
from django.contrib.admin import display

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_children']


class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'get_email', 'age', 'gender', 'get_all_score', 'get_parent']

    @display(description='Name')
    def get_username(self, obj):
        return obj.children_user.username

    @display(description='Email')
    def get_email(self, obj):
        return obj.children_user.email

    @display(description='Score')
    def get_all_score(self, obj):
        return obj.children_score.total_score

    @display(description='Parent')
    def get_parent(self, obj):
        return obj.children_user.parent


class AllScoreAdmin(admin.ModelAdmin):
    list_display = ['kid', 'get_email', 'total_score']

    @display(description='Email')
    def get_email(self, obj):
        return obj.kid.children_user.email


class ShareTokenAdmin(admin.ModelAdmin):
    list_display = ['token', 'children']


admin.site.register(User, UserAdmin)
admin.site.register(ChildrenProfile, ChildrenAdmin)
admin.site.register(AllScore, AllScoreAdmin)
admin.site.register(ShareToken, ShareTokenAdmin)
