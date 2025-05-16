from django.shortcuts import render
from django.http import JsonResponse

from habits.Core.HabitService import create_habit_repository, create_activity_repository, HabitService

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import CreateAPIView
from .serializers import HabitSerializer, HabitActivitySerializer
from .models import Habit, HabitActivity

"""
    habit service     
"""
activity_repository = create_activity_repository()
habit_repository = create_habit_repository()
habit_service = HabitService(activity_repository, habit_repository)

# Create your views here.


class HabitCreateView(APIView):
    def post(self, request):
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HabitDeleteView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = 'habit_id'

class HabitUpdateView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = 'habit_id'

class MarkHabitDoneView(CreateAPIView):
    serializer_class = HabitActivitySerializer
    queryset = HabitActivity.objects.all()
def create_habit(request):
    # TODO: implement
    ...


def remove_habit(request):
    # TODO: implement
    ...


def edit_habit(request):
    # TODO: implement
    ...


def mark_as_done(request):
    # TODO: implement
    ...


# endpoint for testing server status
def index(request):
    return JsonResponse({"status": "success", "server_status": "running"})
