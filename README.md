# College Management System - Backend

This repository contains the backend implementation of a **College Management Application** built using **Django REST Framework** (DRF) with **PostgreSQL** as the database.

## Project Description

The College Management System allows seamless management of students and faculties with two types of users: **Faculty** and **Student**. 

### Features

#### Faculty:
- **Login Access**: 
- **Manage Students**:
  - Create student profiles.
  - View all students.
  - Assign students to themselves.
  - Update student details.

#### Student:
- **Login Access**: 
- **Manage Personal Details**:
  - View personal details, including:
    - Profile picture
    - First Name
    - Last Name
    - Date of Birth
    - Gender
    - Blood Group
    - Contact Number
    - Address
  - Edit personal details.
- **Subjects & Faculty**:
  - View enrolled subjects and corresponding faculty.
  - View related student details.

#### Relationships:
- A faculty can teach multiple students.
- A faculty can teach one subject.
- A student can enroll in multiple subjects.

---

## Tech Stack

- **Backend**: Django with Django REST Framework (DRF)
- **Database**: PostgreSQL
---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.9+**
2. **PostgreSQL**
3. **Pip (Python Package Manager)**
4. **Virtualenv** (optional but recommended)

---

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/shakthi2230/CollegeManagement_Backend.git
cd  project-repo-name

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
Update the `DATABASES` settings in **settings.py** with your PostgreSQL credentials:
```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost', # Or your database host
        'PORT': '5432',      # Default PostgreSQL port
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Start the Development Server
```bash
python manage.py runserver
```
