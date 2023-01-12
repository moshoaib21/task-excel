from .models import  Department,Employee
from urllib import response
from django.http import JsonResponse
from .serializers import EmployeeSerializer,DepartmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET','POST'])
def Emp_list(request ,format=None):
    if request.method == 'GET':
        Hotel=Employee.objects.all()
        serializer=EmployeeSerializer(Hotel,many=True)
        return JsonResponse({'hotel':serializer.data})

    if request.method == 'POST':
        serializer=EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def Emp_details(request,id,format=None):
    try:
        Hotel=Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        serializer=EmployeeSerializer(Employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(Employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def Dep_list(request ,format=None):
    if request.method == 'GET':
        Hotel=Department.objects.all()
        serializer=DepartmentSerializer(Hotel,many=True)
        return JsonResponse({'hotel':serializer.data})

    if request.method == 'POST':
        serializer=DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)