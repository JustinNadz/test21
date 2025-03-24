import json  # Add this import
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Chat  # Ensure correct import

@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for simplicity (not recommended for production)
class ChatView(View):
    def get(self, request):
        chats = Chat.objects.all()
        chat_data = [
            {
                "username": chat.username,
                "chat_message": chat.chat_message,
                "date": chat.date.isoformat() if chat.date else None
            }
            for chat in chats
        ]
        return JsonResponse(chat_data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))  # Parse JSON request
            username = data.get('username')
            chat_message = data.get('chat_message')

            if not username or not chat_message:
                return JsonResponse({"error": "Username and message are required."}, status=400)

            new_chat = Chat.objects.create(username=username, chat_message=chat_message)
            chat_data = {
                "username": new_chat.username,
                "chat_message": new_chat.chat_message,
                "date": new_chat.date.isoformat() if new_chat.date else None
            }
            return JsonResponse(chat_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)