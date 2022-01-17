from django.contrib import admin
from .models import employees
from .models import management

# Register your models here.
admin.site.register(employees)
admin.site.register(management)