from django.test import TestCase
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse

class TestProfileViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Fer',
            email='fer@fer.com',
            password='asdfñlkj',
            first_name='María Fernanda',
            last_name='Mamone'
        )
        self.profile = UserProfile.objects.create(user=self.user)

    def test_profile_list_views(self):
        url = reverse('profile_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  
    
    def test_profile_detail_views(self):
        self.client.login(username='Fer', password='asdfñlkj')
        url = reverse('profile_detail', args=[self.profile.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)       