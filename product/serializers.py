from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.IntegerField()
    background = serializers.CharField()
    alive = serializers.BooleanField()
    
