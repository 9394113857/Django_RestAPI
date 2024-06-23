# Import the necessary module for Django REST framework serializers
from rest_framework import serializers

# Import the Task model from the current application's models
from .models import Task

# Define a serializer for the Task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model that this serializer is associated with (Task model)
        model = Task

        # Specify that you want to include all fields from the Task model
        # Alternatively, you could list specific fields here if you only want to include certain ones
        fields = '__all__'

# This TaskSerializer class allows you to easily serialize and deserialize instances of the Task model 
# to and from various formats such as JSON when working with Django REST framework. 
# The fields = '__all__' line indicates that you want to include all fields
#  from the Task model in the serialized output.
