from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Exercise, Category, Pr
from.serializers import ExerciseSerializer, CategorySerializer, PrSerializer

class CategoryViewSet(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class ExercisesViewSet(ModelViewSet):
  queryset = Exercise.objects.all()
  serializer_class = ExerciseSerializer
  
  def create(self, request):
    serializer = self.serializer_class(data=request.data)
    
    if serializer.is_valid():
      try:
        Category.objects.get(id=request.data["category_id"])
      except:
        return Response({ 
          "data": {}, 
          "errors": { 
            "category": "Categoría no encontrada" 
          } 
        }, status=404)
        
      serializer.save()
      
      return Response({
        "data": serializer.data,
        "errors": {}
      }, status=201)
      
    return Response({
      "data": {},
      "errors": serializer.errors
    }, status=400) 
  
  def list(self, request):
    queryset = list(self.queryset.values())
    
    if len(queryset) == 0:
      return Response({
        "data": [],
        "errors": {}      
      })
    
    for exercise in queryset:
      category = Category.objects.get(id=exercise["category_id"])
      
      exercise["category"] = {
        "id": category.id,
        "name": category.name
      }
      
      del exercise["category_id"]
      
    return Response({ "data": queryset, "errors": {} })
  
class PrViewSet(ModelViewSet):
  queryset = Pr.objects.all()
  serializer_class = PrSerializer