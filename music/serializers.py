from rest_framework import fields, serializers
from .import models 

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Artist
        fields = ('ism','rasm')

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Song
        fields = ('id','nom','cover','source')

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Album
        fields = ('id','nom','muqova')