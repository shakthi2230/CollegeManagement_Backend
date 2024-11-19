from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Assignment, Faculty

class AssignmentDeleteView(APIView):

    def delete(self, request, faculty_id, assignment_id):
        try:
           
            assignment = Assignment.objects.get(id=assignment_id, faculty_id=faculty_id)

            # print(assignment_id)
          
            assignment.delete()

            return Response({
                "message": "Assignment deleted successfully"

            }, status=status.HTTP_204_NO_CONTENT)

        except Assignment.DoesNotExist:
            return Response({
                "message": "Assignment not found or you do not have permission to delete this assignment"
            }, status=status.HTTP_404_NOT_FOUND)
