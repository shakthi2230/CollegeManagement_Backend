from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Assignment, Student
from ...serializers import AssignmentStudentSerializer

class StudentAssignmentView(APIView):

    def get(self, request, student_id):
        try:
         
            student = Student.objects.get(id=student_id)

        except Student.DoesNotExist:
            
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        assignments = Assignment.objects.filter(students=student)
        
      
        serializer = AssignmentStudentSerializer(assignments, many=True)
        
        return Response({
            "message": "Assignments fetched successfully",
            "assignments": serializer.data
        }, status=status.HTTP_200_OK)
