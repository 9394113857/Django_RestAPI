# Import the necessary modules for Django REST framework generics
from rest_framework import generics

# Import the Task model and TaskSerializer from the current application's models and serializers
from .models import Task
from .serializers import TaskSerializer

# Define a view for listing and creating tasks
class TaskList(generics.ListCreateAPIView):
    # Set the queryset to retrieve all Task objects
    queryset = Task.objects.all()

    # Set the serializer class to use for serializing and deserializing Task objects
    serializer_class = TaskSerializer

# Define a view for retrieving, updating, and deleting a single task
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    # Set the queryset to retrieve all Task objects
    queryset = Task.objects.all()

    # Set the serializer class to use for serializing and deserializing Task objects
    serializer_class = TaskSerializer

# These views, TaskList and TaskDetail, are designed to work with the Task model 
# and use the TaskSerializer to handle API requests 
# for listing, creating, retrieving, updating, and deleting tasks. 
# They make use of Django REST framework's generics to provide common functionality for these operations.
