# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from ...serializers import StudentLoginSerializer

# class StudentLoginView(APIView):
#     def post(self, request):
#        
#         serializer = StudentLoginSerializer(data=request.data)

#         if serializer.is_valid():
#             student = serializer.validated_data
#             return Response({
#                 "message": "Login successful",
#                 "student": {
#                     "id": student.id,
#                     "first_name": student.first_name,
#                     "last_name": student.last_name,
#                     "email": student.email,
#                     "dob": student.dob,
#                     "gender": student.gender,
#                     "blood_group": student.blood_group,
#                     "contact_number": student.contact_number,
#                     "address": student.address,
#                     "profile_pic": student.profile_pic.url if student.profile_pic else None
#                 }
#             }, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  ...models import Student
from django.contrib.auth.hashers import check_password
from django.conf import settings

class StudentLoginView(APIView):
    def post(self, request):
       

        print(request.data)

        email = request.data.get('email')
        password = request.data.get('password')

        
        student = Student.objects.filter(email=email).first()

        print(student)

        password_is_correct = student.check_password(password) if student else False

        print("password: ",password_is_correct)

        
        if student and student.check_password(password):
            
            student_data = {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "dob": student.dob,
                "gender": student.gender,
                "blood_group": student.blood_group,
                "contact_number": student.contact_number,
                "address": student.address,
                "profile_pic": student.profile_pic.url if student.profile_pic else None
            }
            
            # print(student_data)

            return Response({
                "message": "Login successful",
                "student": student_data
            }, status=status.HTTP_200_OK)

       
        return Response({
            "message": "Invalid email or password"
        }, status=status.HTTP_400_BAD_REQUEST)
