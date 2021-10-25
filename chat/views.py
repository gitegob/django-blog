from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from chat.models import Room, Message

# Create your views here.


def index(request):
    return render(request, 'chat_index.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat_room.html', {'username': username, 'room_details': room_details, 'room': room})


def check_room(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        print('aaaaaaaaaaaaaaa')
        return redirect('/chat/'+room+'/?username='+username)
    else:
        print('ooooooooooooo')
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    room_id = request.POST['room_id']
    username = request.POST['username']
    room = Room.objects.get(id=room_id)
    new_message = Message.objects.create(
        value=message, user=username, room=room)
    new_message.save()
    return HttpResponse('Message sent successfully')


def get_messages(request, room):
    room = Room.objects.get(name=room)
    messages = room.message_set.all()
    return JsonResponse({'messages': list(messages.values())})
