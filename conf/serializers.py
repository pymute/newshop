from rest_framework.serializers import ModelSerializer
from .models import Student

class NewSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name','last_name','email','password','status','verification_code','profile_image')