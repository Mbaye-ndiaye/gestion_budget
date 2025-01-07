from rest_framework import serializers
from gestionapp.models import CustomUser
from django.contrib.auth import authenticate
from ..models.budget_models import Budget

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'password']

    def create(self, validated_data):
         user = CustomUser.objects.create_user(
             email=validated_data['email'],
             password=validated_data['password'],
             first_name=validated_data['first_name'],
             last_name=validated_data['last_name'],
             phone_number=validated_data['phone_number'],
         )
         Budget.objects.create(user=user, total_amount=0.0)
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




# from rest_framework import serializers
# from ..models.auth_models import CustomUser
# from django.contrib.auth import authenticate
# from ..models.budget_models import Budget
# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             phone_number=validated_data['phone_number'],
#         )
#         Budget.objects.create(user=user, total_amount=0.0)
#         return user
    

# class LoginSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         phone_number = data.get('phone_number')
#         password = data.get('password')

#         if phone_number and password:
#             user = authenticate(phone_number=phone_number, password=password)
#             if user:
#                 if not user.is_active:
#                     raise serializers.ValidationError("Le compte est désactivé.")
#                 return user
#             raise serializers.ValidationError("Numéro de téléphone ou mot de passe invalide.")
#         raise serializers.ValidationError("Les champs 'phone_number' et 'password' sont obligatoires.")
    


