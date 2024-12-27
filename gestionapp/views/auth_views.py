# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from gestionapp.serializers.auth_serializers import RegistrationSerializer, LoginSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth import authenticate

# # Vue pour l'inscription
# class RegistrationView(APIView):
#     """
#     Vue pour l'inscription des utilisateurs avec numéro de téléphone et mot de passe.
#     """
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "Utilisateur créé avec succès."}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Vue pour la connexion avec numéro de téléphone
# class LoginView(APIView):
#     """
#     Vue pour la connexion des utilisateurs avec numéro de téléphone et mot de passe.
#     """
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             phone_number = serializer.validated_data['phone_number']
#             password = serializer.validated_data['password']

#             # Authentification avec le numéro de téléphone
#             user = authenticate(username=phone_number, password=password)  # Django utilise 'username' pour l'identifiant principal
#             if user is not None:
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     "refresh": str(refresh),
#                     "access": str(refresh.access_token),
#                 }, status=status.HTTP_200_OK)
#             return Response({"error": "Numéro de téléphone ou mot de passe invalide."}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Vue pour la déconnexion
# class LogoutView(APIView):
#     """
#     Vue pour la déconnexion des utilisateurs.
#     """
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()  # Invalide le jeton
#             return Response({"message": "Déconnexion réussie."}, status=status.HTTP_200_OK)
#         except Exception:
#             return Response({"error": "Une erreur est survenue lors de la déconnexion."}, status=status.HTTP_400_BAD_REQUEST)





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from gestionapp.serializers.auth_serializers import RegistrationSerializer, LoginSerializer

class RegistrationView(APIView):
    """
    Vue pour l'enregistrement des utilisateurs.
    """
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': RegistrationSerializer(user).data,  # Données utilisateur
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Vue pour la connexion des utilisateurs.
    """
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)