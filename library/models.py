from django.db import models
from accounts.models import User
import time


# artist
class Artist(models.Model):
    name = models.CharField(max_length=25)
    gender = models.IntegerField(default=1)
    local = models.CharField(max_length=25)

    def __str__(self):
        return self.name + ' | ' + self.local


# track
class Track(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    file = models.FileField(upload_to='tracks/', null=True)
    artists = models.ManyToManyField(Artist, related_name='artist_tracks', through='TrackArtist')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)


# many to many relation for Artist-Tracks
class TrackArtist(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['track_id', 'artist_id']

    def __str__(self):
        return self.artist.name + " | " + self.track.title


# album of an artist.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name='artist_albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name + " | " + self.artist.name


# track without album
class SingleTrack(Track):
    def __str__(self):
        return self.title


# track that of album
class AlbumTrack(Track):
    album = models.ForeignKey(Album, related_name='album_tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# list of tracks.
class List(models.Model):
    name = models.CharField(max_length=10, auto_created=True)
    create_at = models.DateField(default=time.time())
    tracks = models.ManyToManyField(Track, through='TracksList')

    def __str__(self):
        return self.name


# many to many relation for list
class TracksList(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['track_id', 'list_id']

    def __str__(self):
        return self.list.name + " | " + self.track.title


# Track List Types:
class PublicList(List):
    pass


class PrivateList(List):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " | " + self.owner.first_name
