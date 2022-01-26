from django.shortcuts import render
from rest_framework import generics
from .models import Feedback
from.serializers import FeedbackSerializer
from .permissions import IsAuthenticatedOrReadOnly

# CR views
class FeedbackList(generics.ListCreateAPIView) :

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
#    permission_classes = (IsAuthenticatedOrReadOnly,)

# RUD view
class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView) :

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
#    permission_classes = (IsAuthenticatedOrReadOnly,)
