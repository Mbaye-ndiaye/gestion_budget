from rest_framework import serializers
from gestionapp.models import CustomUser
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['phone_number'],  # Utilisez le numéro de téléphone comme nom d'utilisateur
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')

        if phone_number and password:
            user = authenticate(phone_number=phone_number, password=password)
            if user:
                return user
            else:
                raise serializers.ValidationError("Numéro de téléphone ou mot de passe invalide.")
        else:
            raise serializers.ValidationError("Les champs 'phone_number' et 'password' sont obligatoires.")
