from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .mypagination import MypaginationClass
# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer
    pagination_class = (MypaginationClass)
    