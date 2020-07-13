from django.contrib import admin

# Register your models here.
from .models import Signup,Login
admin.site.register(Signup)
admin.site.register(Login)
