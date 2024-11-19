from rest_framework import serializers
from .models import  Subject
from .models import Student, Faculty ,Assignment
from django.contrib.auth.hashers import make_password


class FacultySerializer(serializers.ModelSerializer):

    subject_name = serializers.CharField(source='subject.name', read_only=True)  

    class Meta:
        model = Faculty
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'subject_name', 'created_at']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Student

        fields = ['id', 'first_name', 'last_name', 'email', 'dob', 'gender', 'blood_group', 'contact_number', 'address', 'profile_pic', 'password']  # Do not include 'password' in fields

    def create(self, validated_data):
        
        password = validated_data.get('password')

        validated_data['password'] = make_password(password) 

        student = super().create(validated_data)

        return student

    def to_representation(self, instance):
        
        representation = super().to_representation(instance)

        representation.pop('password', None)  

        return representation
    

class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        student = Student.objects.filter(email=email).first()

        if student and student.check_password(password):
            return student  
        raise serializers.ValidationError("Invalid email or password")
    
class StudentUpdateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)

    class Meta:

        model = Student

        fields = ['first_name', 'last_name', 'email', 'dob', 'gender', 'blood_group', 'contact_number', 'address', 'profile_pic', 'password']

    def update(self, instance, validated_data):

        password = validated_data.get('password')

        if password:

            validated_data['password'] = make_password(password)  


        for attr, value in validated_data.items():

            setattr(instance, attr, value)

        instance.save()

        return instance
    
class StudentListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student

        fields = ['id', 'first_name', 'last_name', 'email', 'dob', 'gender', 'blood_group', 'contact_number', 'address', 'profile_pic']


class FacultyUpdateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)  

    class Meta:

        model = Faculty

        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'subject', 'password']

    def update(self, instance, validated_data):

        password = validated_data.get('password', None)
        
        if password:
            instance.set_password(password)  
            
     
        instance.first_name = validated_data.get('first_name', instance.first_name)

        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.email = validated_data.get('email', instance.email)

        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.subject = validated_data.get('subject', instance.subject)
        
        instance.save()

        return instance
    


class AssignmentSerializer(serializers.ModelSerializer):
    faculty_id = serializers.IntegerField(write_only=True)  
    subject_id = serializers.IntegerField(write_only=True)  
    student_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True) 

    faculty = serializers.StringRelatedField(read_only=True)  
    subject = serializers.StringRelatedField(read_only=True)  
    students = serializers.StringRelatedField(many=True, read_only=True)  

    class Meta:

        model = Assignment

        fields = ['faculty_id', 'subject_id', 'student_ids', 'title', 'description', 'due_date', 'faculty', 'subject', 'students',"id"]
    
    def create(self, validated_data):
        

        faculty_id = validated_data.pop('faculty_id')

        subject_id = validated_data.pop('subject_id')

        student_ids = validated_data.pop('student_ids')
        
        faculty = Faculty.objects.get(id=faculty_id)

        subject = Subject.objects.get(id=subject_id)

        students = Student.objects.filter(id__in=student_ids)
        
        assignment = Assignment.objects.create(

            faculty=faculty,

            subject=subject,
            

            title=validated_data['title'],

            description=validated_data['description'],

            due_date=validated_data.get('due_date', None),
        )
        
        assignment.students.set(students)  
        return assignment


# class AssignmentStudentSerializer(serializers.ModelSerializer):

#     faculty = serializers.StringRelatedField(read_only=True)  

#     subject = serializers.StringRelatedField(read_only=True)  
    

#     class Meta:

#         model = Assignment
        
#         fields = ['title', 'description', 'due_date', 'faculty', 'subject']

class AssignmentStudentSerializer(serializers.ModelSerializer):
    faculty_first_name = serializers.SerializerMethodField()  
    subject_name = serializers.CharField(source='faculty.subject.name', read_only=True) 

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date', 'faculty_first_name', 'subject_name']

    def get_faculty_first_name(self, obj):
       
        return obj.faculty.first_name if obj.faculty else None

class FacultyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'subject', 'created_at']