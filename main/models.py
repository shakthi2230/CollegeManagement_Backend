from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class Subject(models.Model):

    name = models.CharField(max_length=255)

    description= models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
   
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject.name if self.subject else 'No Subject'}"
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    
    def authenticate(self, email, password):
        if self.email == email and self.check_password(password):
            return True
        return False
    
class Student(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=4)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    # # Custom authentication method
    # def authenticate(self, email, password):
    #     if self.email == email and self.check_password(password):
    #         return self  # Return the student object if authentication is successful
    #     return None

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='enrolled_students')
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} enrolled in {self.subject.name}"

class Assignment(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='assignments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.subject.name} by {self.faculty.first_name}"