from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ...models import Faculty
from ...serializers import FacultyUpdateSerializer, FacultyDetailSerializer

class FacultyDetailView(generics.RetrieveAPIView):

    queryset = Faculty.objects.all()

    serializer_class = FacultyDetailSerializer

    def get_object(self):
      
        return Faculty.objects.get(pk=self.kwargs['pk'])

    def retrieve(self, request, *args, **kwargs):
        
        obj = self.get_object()

        
        serializer = self.get_serializer(obj)

        
        return Response({
            "faculty": serializer.data
        }, status=status.HTTP_200_OK)
