from django.contrib import admin
from .models import Student,Classes,ClassResources,ClassStudents,Teacher,assignments,AssignmentSubmissions

admin.site.register(Student)
admin.site.register(Classes)
admin.site.register(ClassResources)
admin.site.register(ClassStudents)
admin.site.register(Teacher)
admin.site.register(assignments)
admin.site.register(AssignmentSubmissions)
