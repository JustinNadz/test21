from django.urls import path
from .exam_views import ChatView  # Ensure this import works

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat_view'),
]