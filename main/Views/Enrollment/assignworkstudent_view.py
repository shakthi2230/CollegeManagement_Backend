from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ...serializers import AssignmentSerializer

class AssignWorkToStudentsView(APIView):

    def post(self, request):
        
   
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():

            assignment = serializer.save()  

            return Response({
                'message': 'Assignment created successfully',
                'assignment': AssignmentSerializer(assignment).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
