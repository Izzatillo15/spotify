from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.viewsets import ModelViewSet
from .models import Album, Artist, Song
from .serializers import ArtistSerializer, SongSerializer,AlbumSerializer
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter


class ArtistList(generics.ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["ism",]
    ordering_fields = ["ism"]

class SongList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["nom",]
    ordering_fields = ["nom"]

  

class AlbumAPIView(APIView):
    def get(self,request):
        albums = Album.objects.all()
        al = AlbumSerializer(albums,many=True)
        return Response(al.data)

    def post(self,request):
        al = AlbumSerializer(data=request.data)
        if al.is_valid():
            al.save()
        return Response(al.data,status=status.HTTP_201_CREATED)

class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["nom",]
    ordering_fields = ["nom"]


# class ArtistAPIView(APIView):
#     def get(self,request):
#         artists = Artist.objects.all()
#         ser = ArtistSerializer(artists,many=True)
#         return Response(ser.data)

#     def post(self,request):
#         ser = ArtistSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#         return Response(ser.data,status=status.HTTP_201_CREATED)









