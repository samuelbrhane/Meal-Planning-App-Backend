from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json

@csrf_exempt
def send_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data["email"]
        message = data["message"]
        send_mail(
            "New message from your plate plan website",
            f"From: {email}\n\n{message}",
            email,  # sender
            [settings.EMAIL_HOST_USER],  # recipient(s)
            fail_silently=False,
        )
        return JsonResponse({"message": "Email sent"})
    return JsonResponse({"error": "Invalid request method"})
