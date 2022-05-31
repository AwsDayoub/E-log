from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse
from django.core import serializers
# Create your views here.


def index(request):
    rooms = Room.objects.order_by('date_added')
    return render(request,'ch/index.html',{'rooms':rooms})


def add_room(request):
    return render(request,'ch/add_room.html')

def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request,'room.html',{
        'username': username,
        'room': room,
        'room_details': room_details    
    })


def checkview(request):
    room = request.POST.get('roomname')
    username = request.POST.get('username')
    if Room.objects.filter(name=room).exists():
        return redirect('ch:room',room=room)
    else:
        newroom = Room.objects.create(name=room)
        newroom.save()
        return redirect('ch:room',room=room)


def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')
    new_message = Message.objects.create(message=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message Sent Successfully')

def getMessages(request,room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages':list(messages.values())})