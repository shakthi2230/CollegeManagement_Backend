from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Assignment
from .serializers import AssignmentSerializer

class AssignmentsByFacultyView(APIView):

    def get(self, request, faculty_id):

        assignments = Assignment.objects.filter(faculty_id=faculty_id)

        if not assignments.exists():

            return Response({"message": "No assignments found for this faculty."}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the assignments and return them

        serializer = AssignmentSerializer(assignments, many=True)
        
        return Response({
            "message": "Assignments fetched successfully",
            "assignments": serializer.data
        }, status=status.HTTP_200_OK)
