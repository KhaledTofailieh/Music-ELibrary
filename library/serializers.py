from rest_framework import serializers
from .models import Album, Track, Artist, PublicList, PrivateList, SingleTrack, AlbumTrack


# album without relations:
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'album_name']


# artist without relations:
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


# album with artist;
class ArtistAlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist']


#  track without relations
class TrackSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        try:
            return obj.file.name
        except:
            return None

    class Meta:
        model = Track
        fields = ['id', 'order', 'title', 'duration', 'file_url']


# single track serializer
class SingleTrackSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True, read_only=True)
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        try:
            return obj.file.name
        except:
            return None

    class Meta:
        model = SingleTrack
        fields = ['id', 'order', 'title', 'duration', 'file_url', 'artists']


# single track serializer
class AlbumTrackSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True, read_only=True)
    album = ArtistAlbumSerializer(read_only=True)
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        try:
            return obj.file.name
        except:
            return None

    class Meta:
        model = AlbumTrack
        fields = ['id', 'order', 'title', 'duration', 'file_url', 'album', 'artists']


# public list without relations
class PublicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicList
        fields = ['id', 'name', 'create_at']


class PublicListTracksSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = PublicList
        fields = ['id', 'name', 'create_at', 'tracks']


# album with tracks:
class FullAlbumSerializer(serializers.ModelSerializer):
    album_tracks = TrackSerializer(many=True, read_only=True)
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist', 'album_tracks']


class PrivateSerializer(serializers.ModelSerializer):
    pass


# artist with both tracks and albums.
class FullArtistSerializer(serializers.ModelSerializer):
    artist_albums = AlbumSerializer(many=True,
                                    read_only=True)  # serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    artist_tracks = TrackSerializer(many=True,
                                    read_only=True)  # serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'artist_albums', 'artist_tracks']
