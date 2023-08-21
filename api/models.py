from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, db_column='title')
    description = models.TextField(db_column='description')
    completed = models.BooleanField(default=False, db_column='completed')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Task'
