from django.contrib import admin


from .models.auth_models import CustomUser
admin.site.register(CustomUser)