from django.db import models

class Student(models.Model):
    STATUS_CHOICES = [
        ('md', 'middle'),
        ('jr', 'Junior'),
        ('sr', 'Senior'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=2,choices=STATUS_CHOICES,default='jr')
    verification_code = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='students/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Teacher(models.Model):
    STATUS_CHOICES = [
        ('md', 'middle'),
        ('jr', 'Junior'),
        ('sr', 'Senior'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=2,choices=STATUS_CHOICES,default='jr')
    verification_code = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='students/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Classes(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    featured_image = models.ImageField(upload_to='classes/', null=True, blank=True)
    schedule = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClassStudents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classs = models.ForeignKey(Classes, on_delete=models.CASCADE)

class ClassResources(models.Model):
    classs = models.ForeignKey(Classes, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class assignments(models.Model):
    classs = models.ForeignKey(Classes, on_delete=models.CASCADE)
    description = models.TextField()
    question = models.TextField()
    options = models.JSONField(null=True, blank=True)
    correct_option = models.CharField(max_length=200, null=True, blank=True)
    deadline = models.DateTimeField()
    attachment = models.FileField(upload_to='assignments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AssignmentSubmissions(models.Model):
    assignment = models.ForeignKey(assignments, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='assignments_submissions/', null=True, blank=True)
    selected_option = models.CharField(max_length=200, null=True, blank=True)
    text_input = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)