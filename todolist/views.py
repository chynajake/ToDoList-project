from django.http import HttpResponse  # not sure if I would need this
from .models import Task
from django.contrib.auth.models import User
import json # not sure if I would need this
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .serializers import UserSerializer
from django.shortcuts import render, redirect # not sure if I would need this
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


def task_list(request):
    jsons = {}
    return HttpResponse(
        json.dumps(jsons)
    )


class TaskList(APIView):

    def get(self, request):
        tasks = Task.objects.filter(author = request.user)
        print(tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskUpdate(APIView):
    def get(self, request):
        status = "REQUESTED"
        tasks = Task.objects.filter(executor__exact = request.user.email).filter(status__exact = status)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    def post(self, request):
        task_name = request.data['task']
        content = request.data['content']
        date = request.data['date']
        executor = request.data['executor']
        author = request.user
        status = request.data['status']
        task = Task.objects.get(task = task_name,
                                content = content,
                                date = date,
                                executor = executor,
                                author = author)
        task.status = status
        task.save()
        return Response("1")


class TaskAdd(APIView):
    def post(self, request):
        response = {}
        task_name = request.data['task']
        content = request.data['content']
        date = request.data['date']
        executor = request.data['executor']
        author = request.user
        status = "REQUESTED"
        task = Task.objects.create(task = task_name, content = content, date = date, executor = executor, author = author, status = status)
        task.save()
        response['check'] = "1"
        return Response(response)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserLog(APIView):
    def post(self, request):
        response = {}
        response['check'] = "0"
        username  = request.data['username']
        #email = request.data['email']
        password = request.data['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            response['check'] = "1"
        return Response(response)
class UserLogout(APIView):
    def get(self, request):
        response = {}
        logout(request)
        response['check'] = "1"
        return Response(response)


class UserAdd(APIView):
    #Register new User
    def post(self, request):
        response = {}
        response['check'] = "0"
        print(4*"\t" + "MYLOGS, WE ARE HERE")
        print(4*"\t" + str(request.data['username']))
        #return Response(response)
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        name = request.data['name']
        surname = request.data['surname']
        user = User.objects.create_user(
                                        username,
                                        email,
                                        password
                                        )
        user.first_name = name
        user.last_name = surname
        user.save()

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                response['check'] = "1"
        return Response(response)
