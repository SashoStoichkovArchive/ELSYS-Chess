from django.shortcuts import render


# Create your views here.
def create_game_room(request):
    username = request.user.username
    url = request.build_absolute_uri()

    return render(request, 'game/create_room.html', {
        'title': 'Create room', 'url': url, 'user': username
    })
