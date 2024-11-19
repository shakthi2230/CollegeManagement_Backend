# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from ...models import Student
# from ...serializers import StudentSerializer

# class StudentRegistrationView(APIView):
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)

#         if serializer.is_valid():
#            
#             serializer.save()
#             return Response({
#                 "message": "Student registered successfully",
#                 "student": serializer.data
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Student
from ...serializers import StudentSerializer

class StudentRegistrationView(APIView):
    def post(self, request):
       
        email = request.data.get('email')
        
        if Student.objects.filter(email=email).exists():
            return Response({
                "message": "Email is already registered"
            }, status=status.HTTP_400_BAD_REQUEST)

        
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            
            serializer.save()

            return Response({
                "message": "Student registered successfully",
                "student": serializer.data 
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
