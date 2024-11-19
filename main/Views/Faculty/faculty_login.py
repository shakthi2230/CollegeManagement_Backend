from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Faculty
from ...serializers import FacultySerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken  

class FacultyLoginView(APIView):

    def post(self, request):

        email = request.data.get('email')

        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            faculty = Faculty.objects.get(email=email)
            

        except Faculty.DoesNotExist:
            return Response({"error": "Faculty not found."}, status=status.HTTP_404_NOT_FOUND)

       
        if faculty.authenticate(email, password): 
          
            serializer = FacultySerializer(faculty)
            
           
            # refresh = RefreshToken.for_user(faculty)
            # access_token = str(refresh.access_token)

            # print(serializer.data)

            return Response({
                "message": "Login successful",
                "faculty": serializer.data,
                # "access_token": access_token  
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
