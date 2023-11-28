from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'index.html')

def room(request, chat_room):
    return render(request, "room.html", {"room_name": chat_room})