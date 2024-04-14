from django.contrib.auth import get_user_model
from django.test import TestCase

class UserManagersTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password = 'user')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try: 
            self.assertIsNone(user.username)
        
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='user')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='user')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            self.assertIsNone(admin_user.username)
        except:
            pass
        
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com',
                password='user',
                is_superuser=False
            )
            