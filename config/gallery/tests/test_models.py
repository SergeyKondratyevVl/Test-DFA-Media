from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from gallery.models import Gallery

class GalleryTest(APITestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username='test3', password='1234')

    def test_model(self):
        photo = Gallery.objects.create(to_user=self.user)
        self.assertEqual(photo.to_user_id, self.user.id)
        