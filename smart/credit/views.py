from django.shortcuts import render
from .models import DemandeDePret , Bank 
from .serializers import  DemandeDePretSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.
@api_view(['GET','POST'])
def FBV_List(request):
     # GET
    if request.method == 'GET':
        demandeDePrets = DemandeDePret.objects.all()
        serializer = DemandeDePretSerializer(demandeDePrets, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = DemandeDePretSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


# GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request, pk):
    try:
        demandeDePrets = DemandeDePret.objects.get(pk=pk)
    except DemandeDePret.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = DemandeDePretSerializer(demandeDePrets)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = DemandeDePretSerializer(demandeDePrets, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        demandeDePrets.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
