from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer) :
    class Meta :
        fields = '__all__'
        model = Feedback
        