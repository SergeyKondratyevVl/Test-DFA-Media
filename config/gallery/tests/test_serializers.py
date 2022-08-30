from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from gallery.models import Gallery
from gallery.serializers import UserREADSerializer

User = get_user_model()

class GallerySerializerTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test', password='1234')
    
    def test_user_serializer(self):
        data = UserREADSerializer(self.user).data
        expected_data = {
            'pk': self.user.id,
            'username': 'test',
            'first_name': "",
            'last_name': "",
            'email': "",
            'photos': []
            }
        self.assertEqual(data, expected_data)
    
    def test_user_create_photo(self):
        self.photo = Gallery.objects.create(to_user=self.user)
        Gallery.objects.create(to_user=self.user)
        data = UserREADSerializer(self.user).data
        self.assertEqual(len(data['photos']), 2)
    
    
