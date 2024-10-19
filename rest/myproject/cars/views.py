from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 


class CarViewSet(viewsets.ViewSet):

    def list(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car)
            return Response(serializer.data)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request, pk=None):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
    def destroy(self, request, pk=None):
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
