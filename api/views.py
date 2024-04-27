from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers
from .models import Tasks
from .serializers import TasksSerializer

# Create your views here.


@api_view(['GET'])
def GetTasks(request):
    tasks = Tasks.objects.all()
    serializer = TasksSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateTasks(request):
    data = request.data
    task = Tasks.objects.create(
        body = data['body']
    )
    serializer = TasksSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def PutTasks(request, pk):
    data = request.data
    taskW = Tasks.objects.get(id=pk)
    serializer = TasksSerializer(instance=taskW, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTasks(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return Response('Tarea Eliminada')