from .models import *
from rest_framework import serializers
class loginserializer(serializers.Serializer):
 useername = serializers.CharField()
 password = serializers.CharField()
