from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from gallery.models import Gallery

User = get_user_model()

class APIViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='root', password='1234')
        self.photo_1 = Gallery.objects.create(to_user=self.user)
        self.photo_2 = Gallery.objects.create(to_user=self.user)

        self.user_2 = User.objects.create_user(username='root2', password='1234')
        self.photo_3 = Gallery.objects.create(to_user=self.user_2)

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_register(self):
        data = {'username': 'test',
                'password': '1234',
                'email': 'test@mail.ru',
                'first_name': 'test_first_name',
                'last_name': 'test_last_name'}
        url = reverse('register')
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['username'], "test")
        self.assertEqual(resp.data['email'], "test@mail.ru")
        self.assertEqual(resp.data['first_name'], "test_first_name")
        self.assertEqual(resp.data['last_name'], "test_last_name")
    
    def test_gallery_list(self):
        url = reverse('gallery-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 3)
    
    def test_gallery_post(self):
        url = reverse('gallery-post')
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 201)
        self.assertIsNone(resp.data['profile_photo'])
    
    def test_gallery_detail(self):
        url = reverse('gallery-detail', kwargs={'pk': 1})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNone(resp.data['profile_photo'])
        self.assertIsNotNone(resp.data['changed'])
        self.assertIsNotNone(resp.data['created'])
    
    def test_user(self):
        url = reverse('user', kwargs={'username': 'root2'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['pk'], self.user_2.pk)
        self.assertEqual(resp.data['username'], 'root2')
        self.assertEqual(len(resp.data['photos']), 1)
    
    def test_photo_detail(self):
        url = reverse('photo-detail', kwargs={'username': 'root2', 'pk': '3'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['pk'], 3)
        self.assertIsNone(resp.data['profile_photo'])
        self.assertIsNotNone(resp.data['changed'])
        self.assertIsNotNone(resp.data['created'])
    
    def test_photo_detail_delete_not_author(self):
        url = reverse('photo-detail', kwargs={'username': 'root2', 'pk': '3'})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 403)
    
    def test_photo_detail_patch_not_author(self):
        url = reverse('photo-detail', kwargs={'username': 'root2', 'pk': '3'})
        resp = self.client.patch(url)
        self.assertEqual(resp.status_code, 403)
    
    def test_photo_detail_delete_author(self):
        url = reverse('photo-detail', kwargs={'username': 'root', 'pk': '1'})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)
    
    def test_photo_detail_patch_author(self):
        url = reverse('photo-detail', kwargs={'username': 'root', 'pk': '1'})
        resp = self.client.patch(url)
        self.assertEqual(resp.status_code, 200)
    
    def test_not_authenticated(self):
        url = reverse('gallery-list')
        client = APIClient()
        resp = client.get(url)
        self.assertEqual(resp.status_code, 403)
    
    def test_delete_all(self):
        url = reverse('delete-all')
        client = APIClient()
        self.superuser = User.objects.create_superuser(username='roo3', password='1234')
        client.force_authenticate(self.superuser)
        resp = client.delete(url)
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(Gallery.objects.count(), 0)
         