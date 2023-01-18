from rest_framework import serializers
from .models import ImagePrediction

class ImagePredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePrediction
        fields = '__all__'
        read_only_fields = ["predictions"]