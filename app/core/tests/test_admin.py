from django.test import TestCase, Client  # test client that will allow us
  # to make test requests to our application in our unit tests
from django.contrib.auth import get_user_model  #
from django.urls import reverse  # reverse which will allow us to
  # generate URLs for our Django admin page


class AdminSiteTests(TestCase):

    def setUp(self):  # it is is a function that is ran before every test that we
      # run so sometimes there are setup tasks that need to be done
      # before every test in our test case class.

        self.client = Client()  # create a new user. It is set to self so that it is accessible
         # in the other test client variable
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@doodle.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)  # make sure the user is logged
          # into our client.
          # so what this does is it uses the client helper function that allows
          # you to log a user in with the Django authentication and this really helps
          # make our tests a lot easier to write because it means we don't have to
          # manually log the user in we can just use this helper function.

        self.user = get_user_model().objects.create_user(
            email='test@doodle.com',
            password='password123',
            name='Test user full name'
        )

        """ Okay so now we have a client, an admin. The admin is
        logged into the client and we have a spare user here that we can use for
        testing listing and things like that."""


    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')  #
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        #/admin/core/user/
        res = self.client.get(url) #going to do a http get on the url

        self.assertEqual(res.status_code, 200) #http 200

    def test_create_user_page(self):  # adding new user in the django admin
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url) #going to do a http get on the url

        self.assertEqual(res.status_code, 200) #http 200
