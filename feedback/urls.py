from django.urls import path
from .views import FeedbackList, FeedbackDetail

urlpatterns = [
    path('', FeedbackList.as_view(), name = 'feedback_list'),
    path('<int:pk>/', FeedbackDetail.as_view(), name = 'feedback_detail' )
]
