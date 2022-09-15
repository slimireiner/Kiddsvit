import secrets
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = 'accounts_users'


class Children(models.Model):
    class Meta:
        db_table = 'accounts_children'

    GENDERS = {'male', 'female', 'unknown'}

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='childrens')

    def assign_to_course(self, course: object):
        self.course_rels.create(course=course)
        for task in course.tasks.all():
            self.children_task_progress_rels.create(task=task) # TODO Bulk create

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class AllScore(models.Model):
    class Meta:
        db_table = 'accounts_children_scores'

    kid = models.OneToOneField(Children, on_delete=models.CASCADE, related_name='children_score')
    total_score = models.IntegerField(default=0)

    def add_score(self, score: int) -> None:
        self.total_score += score
        self.save(update_fields=['total_score'])

    def __str__(self):
        return self.kid.name


class ShareToken(models.Model):
    token = models.CharField(max_length=256)
    children = models.ForeignKey(Children, on_delete=models.CASCADE, related_name='shore_tokens')

    def __str__(self):
        return self.children.name
