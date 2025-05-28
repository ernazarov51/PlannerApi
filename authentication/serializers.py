from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField
from rest_framework.exceptions import ValidationError
from authentication.models import User


class UserRegisterModelSerializer(ModelSerializer):
    confirm_password=CharField(write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','phone_number','email','username','password','confirm_password']
        extra_kwargs={
            'last_name':{'required':False},
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password=attrs.get('password')
        confirm_password=attrs.get('confirm_password')
        if password !=confirm_password:
            raise ValidationError('passwords is not equal')
        return attrs

    def create(self, data):
        password=data['password']
        data.pop('confirm_password')
        data['password']=make_password(password)
        return User.objects.create(**data)




