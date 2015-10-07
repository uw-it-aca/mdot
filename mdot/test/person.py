from django.contrib.auth.models import User
from django.test import Client, TestCase


class MDOTPersonTest(TestCase):
    """ Tests functionality around getting information about the user once he or
        she logs in.
    """
    def setUp(self):
        pass

    def test_get_affiliation_from_username(self):
        # create a user
        javerage = User.objects.create_user('javerage',
                                            'javerage@uw.edu',
                                            'mytestpass')

        # log the user in
        client = Client()
        response = client.post('/login/',
                               {'username': 'javerage',
                                'password': 'mytestpass',
                                'next': '/'},
                               follow=True)

        self.assertEqual(200, response.status_code)
        self.assertInHTML(('<div aria-hidden="true" class="mdot-netid">'
                           '<span id="mdot_user_button">javerage</span>'
                           '</div>'),
                          response.content)

        # assert that the DAO can return affiliation information

    def tearDown(self):
        pass
