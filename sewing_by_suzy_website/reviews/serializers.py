from rest_framework import serializers
from .models import Reviews

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Reviews
        fields = ['id', 'name', 'date', 'number_rating', 'comment']