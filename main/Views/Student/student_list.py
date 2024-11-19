# views.py
from rest_framework import generics
from ...models import Student
from ...serializers import StudentListSerializer

class StudentListView(generics.ListAPIView):
    
    queryset = Student.objects.all()

    serializer_class = StudentListSerializer
