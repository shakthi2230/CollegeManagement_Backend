from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ...models import Faculty
from ...serializers import FacultyUpdateSerializer

class FacultyUpdateView(generics.UpdateAPIView):

    queryset = Faculty.objects.all()
    
    serializer_class = FacultyUpdateSerializer

    def get_object(self):
        
        return Faculty.objects.get(pk=self.kwargs['pk'])

    def update(self, request, *args, **kwargs):
     
        obj = self.get_object()
        
       
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        
        if serializer.is_valid():
           
            serializer.save()
            
            
            return Response({
                "message": "Faculty updated successfully",
                "faculty": serializer.data
            }, status=status.HTTP_200_OK)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
