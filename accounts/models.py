import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = 'accounts_users'
    is_children = models.BooleanField(null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', null=True, default=None)
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class ChildrenProfile(models.Model):
    class Meta:
        db_table = 'accounts_children'

    GENDERS = {'male', 'female', 'unknown'}

    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    children_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='children_profile')

    def assign_to_course(self, course: object):
        self.course_rels.create(course=course)
        for task in course.tasks.all():
            self.children_task_progress_rels.create(task=task)
            # TODO Bulk create

    def __str__(self):
        return self.children_user.username

    def __repr__(self):
        return self.children_user.username


class AllScore(models.Model):
    class Meta:
        db_table = 'accounts_children_scores'

    kid = models.OneToOneField(ChildrenProfile, on_delete=models.CASCADE, related_name='children_score')
    total_score = models.IntegerField(default=0)

    def add_score(self, score: int) -> None:
        self.total_score += score
        self.save(update_fields=['total_score'])

    def __str__(self):
        return self.kid.children_user.username

    def get_score_token(self, children_id: int):
        if self.kid_id == children_id:
            stats = [{'name': self.kid.children_user.username,
                      'score': self.total_score,
                      'parent': self.kid.children_user.parent.username}]
        return stats


class ShareToken(models.Model):
    token = models.CharField(max_length=256)
    children = models.ForeignKey(ChildrenProfile, on_delete=models.CASCADE, related_name='shore_tokens')

    def __str__(self):
        return self.children.children_user.username


class UserProfile(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone_numbers = models.IntegerField()
    age = models.IntegerField()

