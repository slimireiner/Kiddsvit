from datetime import datetime

from django.db import models

from accounts.models import ChildrenProfile


class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_progress(self):
        in_progress = 0
        done = 0
        for task in self.tasks.prefetch_related('progress').all():
            if task.progress.first().task_status == TaskProgress.statuses[0][0]:
                in_progress += 1
            elif task.progress.first().task_status == TaskProgress.statuses[1][0]:
                done += 1
        return in_progress, done, self.tasks.count()


class Task(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks')
    content = models.TextField()

    def __str__(self):
        return self.name


class TaskProgress(models.Model):
    statuses = (
        ('assign', 'Assign'),
        ('in_progress', 'In progress'),
        ('done', 'Done')
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='progress')
    created_ad = models.DateTimeField(null=True, default=None)
    finished_ad = models.DateTimeField(null=True, default=None)
    task_status = models.CharField(max_length=50, choices=statuses, default=statuses[0][0])
    children = models.ForeignKey(ChildrenProfile, on_delete=models.CASCADE, related_name='children_task_progress_rels')

    def __str__(self):
        return self.task.name

    def change_status_task(self, status: str = statuses[1][0]) -> None:
        self.task_status = status
        if status == self.statuses[2][0]:
            self.children.children_score.add_score(self.task.score)
        elif status == self.statuses[1][0]:
            pass
        else:
            raise Exception('Bad status')
        self.save(update_fields=['task_status'])

    def is_all_tasks_done(self):
        tasks = TaskProgress.objects.filter(children=self.children_id, task__course_id=self.task.course_id).all()
        return all([task.task_status == 'done' for task in tasks])


class ChildrenCourseRelation(models.Model):
    children = models.ForeignKey(ChildrenProfile, on_delete=models.CASCADE, related_name='course_rels')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='children_rels')
    created_ad = models.DateTimeField(null=True, default=None)
    finished_ad = models.DateTimeField(null=True, default=None)

    def finish(self):
        self.finished_ad = datetime.now()
        self.save(update_fields=['finished_ad'])
