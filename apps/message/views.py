from django.shortcuts import render

# Create your views here.
from message.models import UserMessage


def get_form(request):
    if request.method == 'POST':
        name = request.POST
    UserMessage.objects.filter()
    return render(request, 'message_form.html')