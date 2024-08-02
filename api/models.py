# Import the necessary module for Django models
from django.db import models

# Define a Django model called 'Task'
class Task(models.Model):
    # Create a field 'title' for the task with a maximum length of 200 characters
    title = models.CharField(max_length=200, verbose_name='Title', db_column='title')

    # Create a field 'description' for the task, which can hold a longer text
    description = models.TextField(verbose_name='Description', db_column='description')

    # Create a field 'completed' for the task, representing whether the task is completed or not
    # It has a default value of False, indicating the task is initially not completed
    completed = models.BooleanField(default=False, verbose_name='Completed', db_column='completed')

    # Define a human-readable string representation of the task
    def __str__(self):
        return self.title

    # Define the database table name for this model, which will be 'Task'
    class Meta:
        db_table = 'Task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

# Additional comments
# 1) This Django model represents tasks with three fields: title, description, and completed.
# The title field is a character field with a maximum length of 200 characters.
# The description field is a text field for longer descriptions of the task.
# The completed field is a boolean field with a default value of False, indicating that tasks are initially not completed.

# 2) The __str__ method is defined to provide a human-readable string representation of a Task object,
# which is based on the task's title.

# 3) The class Meta inside the model is used to specify the database table name for this model, 
# which is set to 'Task'. This allows you to control the name of the database table associated with the model.
