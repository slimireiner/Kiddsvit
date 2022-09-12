from django.db import models

from accounts.models import AllScore


class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_progress(self):
        in_progress = 0
        done = 0
        for task in self.tasks.prefetch_related('progress').all():
            if task.progress.first().task_status == Progress.statuses[0][0]:
                in_progress += 1
            elif task.progress.first().task_status == Progress.statuses[1][0]:
                done += 1
        return in_progress, done, self.tasks.count()


class Task(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name


class Progress(models.Model):
    statuses = (
        ('in_progress', 'In progress'),
        ('done', 'Done')
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='progress')
    task_status = models.CharField(max_length=50, choices=statuses, default=statuses[0][0])
    children = models.ForeignKey(AllScore, on_delete=models.CASCADE, related_name='children_total_score')

    def __str__(self):
        return self.task.name

    def change_status_task(self, status: str = statuses[0][0]) -> None:
        self.task_status = status
        if status == self.statuses[1][0]:
            self.children.add_score(self.task.score)
        self.save(update_fields=['task_status'])
