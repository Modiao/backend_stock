from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from .models import Customer, Ticket

class RegisterUserSerializer(serializers.ModelSerializer):
    """ This will help us to create a User and check the validation """

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, 
        validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('usernamle', 'password', 'password2', 'eemail', 'firs_name', 'last_name')
        extra_kwargs = {
            'first_name' : {'required': True},
            'last_name' : {'required': True}
        }

    def validate(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
            email=validate_data['email'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name']
        )

        user.set_password(validate_data['password'])
        user.save()
        return user

class ListUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class UpdateTicketSerializer(serializers.Serializer):
    id_ticket = serializers.CharField()
    is_valid = serializers.BooleanField()