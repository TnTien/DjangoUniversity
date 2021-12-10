from django.contrib import admin

# Register your models here.
#   Allows access to classApp through the admin page.
from .models import djangoClasses

admin.site.register(djangoClasses)
