from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import serializers
from .models import Track, Album, Artist, PublicList, PrivateList, SingleTrack, AlbumTrack


# Create your views here.
def get_tracks(request):
    tracks = Track.objects.all()
    serialized = serializers.TrackSerializer(instance=tracks, many=True)
    return JsonResponse(serialized.data, safe=False)


def get_albums(request):
    albums = Album.objects.all()
    serialized = serializers.ArtistAlbumSerializer(instance=albums, many=True)
    print(serialized.data)
    return JsonResponse(serialized.data, safe=False)


def get_track(request, track_id):
    try:
        track = SingleTrack.objects.get(id=track_id)
        serialized = serializers.SingleTrackSerializer(instance=track)
    except:
        track = AlbumTrack.objects.get(id=track_id)
        serialized = serializers.AlbumTrackSerializer(instance=track)

    return JsonResponse(serialized.data, safe=False)


def get_album(request, album_id):
    album = Album.objects.get(id=album_id)
    serialized = serializers.FullAlbumSerializer(instance=album)
    return JsonResponse(serialized.data, safe=False)


def get_artists(request):
    artists = Artist.objects.all()
    serialized = serializers.ArtistSerializer(instance=artists, many=True)
    return JsonResponse(serialized.data, safe=False)


def get_artist(request, artist_id):
    artists = Artist.objects.get(id=artist_id)
    serialized = serializers.FullArtistSerializer(instance=artists)
    return JsonResponse(serialized.data, safe=False)


def get_lists(request):
    public_lists = PublicList.objects.all()
    private_lists = PrivateList.objects.all()

    public_serialized = serializers.PublicListSerializer(instance=public_lists, many=True)
    private_serialized = serializers.PublicListSerializer(instance=private_lists, many=True)

    lists = {
        'private': private_serialized.data,
        'public': public_serialized.data
    }
    return JsonResponse(lists, safe=False)


def get_list(request, list_id):
    try:
        list_ = PublicList.objects.get(id=list_id)
    except:
        o_id = 1
        list_ = PrivateList.objects.get(owner_id=o_id, id=list_id)

    serialized = serializers.PublicListTracksSerializer(instance=list_)
    return JsonResponse(serialized.data, safe=False)


def get_public_lists(request):
    lists = PublicList.objects.all()
    serialized = serializers.PublicListSerializer(instance=lists, many=True)
    return JsonResponse(serialized.data, safe=False)


def get_public_list(request, list_id):
    list_ = PublicList.objects.get(id=list_id)
    serialized = serializers.PublicListTracksSerializer(instance=list_)
    return JsonResponse(serialized.data, safe=False)


def get_private_lists(request):
    o_id = 1
    lists = PrivateList.objects.filter(owner_id=o_id)
    serialized = serializers.PublicListSerializer(instance=lists, many=True)
    return JsonResponse(serialized.data, safe=False)


def get_private_list(request, list_id):
    o_id = 1
    list_ = PrivateList.objects.get(owner_id=o_id, id=list_id)
    serialized = serializers.PublicListTracksSerializer(instance=list_)
    return JsonResponse(serialized.data, safe=False)
