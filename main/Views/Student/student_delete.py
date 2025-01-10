
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from ...models import Student
from ...serializers import StudentListSerializer

class StudentDeleteView(generics.DestroyAPIView):
    
    queryset = Student.objects.all()

    serializer_class = StudentListSerializer

    def get_object(self):
        try:
            return Student.objects.get(pk=self.kwargs['pk'])
        
        except Student.DoesNotExist:

            raise NotFound(detail="Student not found")
    
    def destroy(self, request, *args, **kwargs):
        
        student = self.get_object()

        student.delete()  
       
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_200_OK)
