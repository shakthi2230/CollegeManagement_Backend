# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from ...models import Student
from ...serializers import StudentUpdateSerializer

class StudentUpdateView(APIView):
    def put(self, request, pk):
      
        try:
            student = Student.objects.get(pk=pk)

        except Student.DoesNotExist:

            raise NotFound(detail="Student not found")

    
        serializer = StudentUpdateSerializer(student, data=request.data, partial=True)  

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Student updated successfully",
                "student": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        
        try:
            student = Student.objects.get(pk=pk)

        except Student.DoesNotExist:
            
            raise NotFound(detail="Student not found")

        serializer = StudentUpdateSerializer(student, data=request.data, partial=True) 

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Student updated successfully",
                "student": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
