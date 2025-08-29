# Import the necessary module for defining URL patterns
from django.urls import path

# Import the views 'TaskList' and 'TaskDetail' from your application's views module
from .views import TaskList, TaskDetail

# Define the URL patterns for your application
urlpatterns = [
    # Define a URL pattern for listing and creating tasks
    path('tasks/', TaskList.as_view(), name='task-list'),

    # Define a URL pattern for retrieving, updating, and deleting a single task
    # The '<int:pk>/' part is a URL parameter that represents the primary key of the task
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]

# These URL patterns specify the paths that users can access to perform different actions on tasks. 
# For example, accessing '/tasks/' will route the request to the TaskList view 
# for listing and creating tasks, 
# and accessing '/tasks/1/' will route the request to the TaskDetail view for a specific task 
# with a primary key of 1 (you can replace 1 with the primary key of the task you want to access). 
# The name parameter provides a name to each URL pattern, 
# which can be useful for reverse URL lookups in your Django application.
