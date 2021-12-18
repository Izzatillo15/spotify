from django.test import TestCase

from next.models import Artist,Album,Song


class TestArtistSerializer(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(ism="Islomjon Islomjon", rasm="islomjon.jpg")
    def test_data(self):
        data = ArtistSerializer(self.actor).data
        self.assertIsNotNone(data)
        assert data['id']is not None
        assert data['ism'] == "Islomjon Islomjon"
        assert data['rasm'] =="islomjon.jpg"

class TestAlbumSerializer(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(ism="Islomjon Islomjon", rasm="islomjon.jpg")
        self.album = Album.objects.create()
        self.artist.album.add(self.artist)
    def test_album(self):
        assert True

 class TestArtistValidation(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Ali",password="Admin")
        self.artist = Artist.objects.create(name="Raj Kapoor", gender="Male", birth_date="1986-12-02")
        self.album = Album.objects.create(genre="Action", name="Kelinlar qozgoloni", year="2011-02-09", imdb=3.4)
        self.artist.album.add(self.artist)
    def test_is_not_Valid(self):
        data= {
            "id":1,
            "album":self.album.id,
            "user":self.user.id,
            "text":"Juda bir yaxshi kino ishlashipti"
        }
        ser = ArtistSerializer(data=data)
        self.assertTrue(ser.is_valid())
       