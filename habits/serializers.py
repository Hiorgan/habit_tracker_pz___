from rest_framework import serializers
from .models import Habit, HabitActivity
from datetime import date

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['habit_id', 'name', 'user_id', 'activity_value_type']

    def validate_activity_value_type(self, value):
        if value not in ['int', 'float']:
            raise serializers.ValidationError("activity_value_type musi być 'int' lub 'float'")
        return value

class HabitActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitActivity
        fields = ['id', 'habit', 'activity_date']
        extra_kwargs = {'activity_date': {'required': False}}

    def create(self, validated_data):
        if 'activity_date' not in validated_data:
            validated_data['activity_date'] = date.today()
        return super().create(validated_data)
