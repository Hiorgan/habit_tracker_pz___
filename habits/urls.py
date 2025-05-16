from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="server_status"),
    path("habits/", views.HabitCreateView.as_view(), name="habit-create"),
    path("habits/<int:habit_id>/", views.HabitDeleteView.as_view(), name="habit-delete"),
    path("habits/<int:habit_id>/edit/", views.HabitUpdateView.as_view(), name="habit-update"),
    path("habits/mark-done/", views.MarkHabitDoneView.as_view(), name="habit-mark-done"),
]
