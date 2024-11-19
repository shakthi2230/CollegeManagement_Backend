from django.urls import path
# from .views import FacultyLoginView
from .Views.Faculty.faculty_login import FacultyLoginView
from .Views.Faculty.faculty_update import FacultyUpdateView
from .Views.Student.student_registration import StudentRegistrationView
from .Views.Student.student_login import StudentLoginView
from .Views.Student.student_update import StudentUpdateView
from .Views.Student.student_list import StudentListView
from .Views.Student.student_delete import StudentDeleteView

from .Views.Enrollment.assignworkstudent_view import AssignWorkToStudentsView
from .Views.Enrollment.studentassignmentview import StudentAssignmentView
from .Views.Enrollment.assignmentbyfacultyview import AssignmentsByFacultyView
from .Views.Enrollment.AssignmentDeleteView import AssignmentDeleteView

# from .views import StudentUpdateView
# from .views import StudentRegistrationView
# from .views import StudentLoginView
# from .views import StudentListView
# from .views import StudentDeleteView
# from .views import FacultyUpdateView
# from .views import AssignWorkToStudentsView
# from .views import StudentAssignmentView
# from .views import AssignmentsByFacultyView
from .Views.Faculty.facultydetailview import FacultyDetailView


urlpatterns = [
    path('faculty/login/', FacultyLoginView.as_view(), name='faculty-login'),
     path('faculty/<int:pk>/update/', FacultyUpdateView.as_view(), name='faculty-update'),

    path('student/register/', StudentRegistrationView.as_view(), name='student-register'),
    path('student/login/', StudentLoginView.as_view(), name='student-login'),
    path('student/update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    path('assign-work/', AssignWorkToStudentsView.as_view(), name='assign-work'),
    path('student/<int:student_id>/assignments/', StudentAssignmentView.as_view(), name='student-assignments'),
    path('faculty/<int:faculty_id>/assignments/', AssignmentsByFacultyView.as_view(), name='assignments-by-faculty'),
    path('faculty/<int:faculty_id>/assignments/<int:assignment_id>/delete/', AssignmentDeleteView.as_view(), name='delete-assignment'),

     path('faculty/<int:pk>/', FacultyDetailView.as_view(), name='faculty-detail'),
]

