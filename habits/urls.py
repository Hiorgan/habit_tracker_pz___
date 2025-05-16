from django.urls import path
from .views import HabitCreateView
from .views import HabitDeleteView
from .views import HabitUpdateView, MarkHabitDoneView

from . import views

urlpatterns = [
    path("", views.index, name="server_status"),
    path('habits/', HabitCreateView.as_view(), name='habit-create'),
    path('habits/<int:habit_id>/', HabitDeleteView.as_view(), name='habit-delete'),
    path('habits/<int:habit_id>/edit/', HabitUpdateView.as_view(), name='habit-update'),
    path('habits/mark-done/', MarkHabitDoneView.as_view(), name='habit-mark-done'),
]
