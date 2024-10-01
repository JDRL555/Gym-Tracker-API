from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid

class UpdatedAtField(models.TimeField):
  def pre_save(self, model_instance, add):
    return now()

# Create your models here.
class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)
  created_at = models.DateField(default=now)
  updated_at = UpdatedAtField(default=now)
  
  def __str__(self):
    return self.name
  
class Exercise(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=200)
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
  created_at = models.DateField(default=now)
  updated_at = UpdatedAtField(default=now)
  
  def __str__(self):
    return self.name
  
class Pr(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  reps = models.IntegerField()
  weight = models.DecimalField(max_digits=20, decimal_places=2)
  created_at = models.DateField(default=now)
  updated_at = UpdatedAtField(default=now)
  
  def __str__(self):
    return f"{self.user_id.first_name} - {self.exercise_id.name}: {self.reps}, {self.weight}kg"