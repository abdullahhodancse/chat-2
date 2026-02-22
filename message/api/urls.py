from django.urls import path
from message.api.view.message_history import ChatHistoryView

urlpatterns = [
    path('<str:room_name>/', ChatHistoryView.as_view()),
]