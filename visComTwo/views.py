# all end points are created here
# imports request method
from django.http import JsonResponse
# imports VisualCard from models file
from .models import VisualCard
# imports VisualCardSerializer from serializer file
from .serializers import VisualCardSerializer
# imports api_view decorator
from rest_framework.decorators import api_view
# imports the response for post
from rest_framework.response import Response
# imports status for post
from rest_framework import status

# use this decorator so the function below takes multiple request types (CRUD)
@api_view(['GET', 'POST'])
def visual_card_list(request, format= None):
    # get all visual cards
    if request.method == 'GET':
        visual_cards = VisualCard.objects.all()
        # serialize them (create instance of VisualCardSerializer class); this serializes all of them because we have a list
        serializer = VisualCardSerializer(visual_cards, many=True)
        # return the json (in order to allow non-dictionary objects to be serialized set the safe parameter to False)
        # return JsonResponse(serializer.data, safe= False)
        return Response(serializer.data)
    
    # post new visual card
    if request.method == 'POST':
        # pass in data from the request
        serializer = VisualCardSerializer(data= request.data)
        # check if data sent is valid, save it
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
# use this decorator so the function below takes multiple request types (CRUD)
@api_view(['GET', 'PUT', 'DELETE'])
# takes in a request and id to get
def visual_card_detail(request, id, format= None):
    # assign id to pk (primary key) parameter
    # the try/except checks if it is a valid request
    try:
        visual_card = VisualCard.objects.get(pk= id)
    except VisualCard.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    # gets 1 visual card
    if request.method == 'GET':
        serializer = VisualCardSerializer(visual_card)
        return Response(serializer.data)
    
    # updates a visual card
    elif request.method == 'PUT':
        serializer = VisualCardSerializer(visual_card, data= request.data)
        # check if data sent is valid, save it
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # else, send this error message
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    # deletes a visual card
    elif request.method == 'DELETE':
        visual_card.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



# from here, go to urls.py to create url

# if error with rest_framework: check interpreter (command+shift+p > select interpreter > python select interpreter > recommended venv instead of global venv)