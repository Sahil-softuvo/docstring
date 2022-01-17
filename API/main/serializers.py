from rest_framework import serializers
from .models import employees
from .models import management

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model= employees
        fields = '__all__'


class managementserializer(serializers.ModelSerializer):

    class Meta:
        model= management
        fields = '__all__'