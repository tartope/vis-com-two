# describes the process of going from a python object to json
from rest_framework import serializers
from .models import VisualCard

# we use this serializer to return our model through our API
class VisualCardSerializer(serializers.ModelSerializer):
    # create inner class with metadata describing the model
    class Meta:
        model = VisualCard
        fields = ['id', 'name', 'image']


# from here, we must create end point; begin by creating views.py