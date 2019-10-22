from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums
    }
    return render(request, 'Music/index.html', context)


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'Music/detail.html', {'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExists):
        return  render(request, 'Music/detail.html', {
            'album': album,
            'error_message': "You did not select any song"
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'Music/detail.html', {'album': album})