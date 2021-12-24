from django.contrib import admin
from .models import Album, AlbumTrack, SingleTrack, Artist, Track, List, PrivateList, PublicList, TracksList, TrackArtist

# Register your models here.
admin.site.register(Album)
admin.site.register(AlbumTrack)
admin.site.register(SingleTrack)
admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(List)
admin.site.register(PrivateList)
admin.site.register(PublicList)
admin.site.register(TracksList)
admin.site.register(TrackArtist)


