from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Exercise, Pr

class CategorySerializer(serializers.Serializer):
  class Meta:
    model = Category
    fields = ["id", "name", "created_at", "updated_at"]

class ExerciseSerializer(serializers.Serializer):
  category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
  class Meta:
    model = Exercise
    fields = [
      "id",
      "name",
      "category_id",
      "created_at",
      "updated_at"
    ]
    
class PrSerializer(serializers.Serializer):
  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
  exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all(), required=True)
  class Meta:
    model = Pr
    fields = [
      "id",
      "exercise_id",
      "user_id",
      "reps",
      "weight",
      "created_at",
      "updated_at"
    ]