from sop.models import *
from rest_framework import serializers

class RegistrS(serializers.ModelSerializer):

    class Meta:
        db_table = 'Registr'
        model = Registr
        abstract = True
        fields = '__all__'