from datetime import date

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

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


def index(request):
    Habit.objects.get_or_create(
        habit_id=1,
        defaults={
            "name": "Test Habit",
            "user_id": 1,
            "activity_value_type": "int"
        }
    )
    return HttpResponse("Test habit created if not already existing.")

# POST /api/habits/
class HabitCreateView(APIView):
    def post(self, request):
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE /api/habits/<habit_id>/
class HabitDeleteView(APIView):
    def delete(self, request, habit_id):
        try:
            habit = Habit.objects.get(pk=habit_id)
            habit.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Habit.DoesNotExist:
            return Response({"error": "Habit not found."}, status=status.HTTP_404_NOT_FOUND)

# PUT /api/habits/<habit_id>/edit/
class HabitUpdateView(APIView):
    def put(self, request, habit_id):
        try:
            habit = Habit.objects.get(habit_id=habit_id)
        except Habit.DoesNotExist:
            return Response({"detail": "Habit not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HabitSerializer(habit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST /api/habits/mark-done/
class MarkHabitDoneView(APIView):
    def post(self, request):
        habit_id = request.data.get('habit_id')
        try:
            habit = Habit.objects.get(habit_id=habit_id)
        except Habit.DoesNotExist:
            return Response({"detail": "Habit not found."}, status=status.HTTP_404_NOT_FOUND)

        habit_activity = HabitActivity(
            habit_id=habit.habit_id,
            activity_date=date.today()
        )
        habit_activity.save()
        return Response({"detail": "Habit marked as done."}, status=status.HTTP_201_CREATED)
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
#def index(request):
#    return JsonResponse({"status": "success", "server_status": "running"})
