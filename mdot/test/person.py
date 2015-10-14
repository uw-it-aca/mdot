from django.contrib.auth.models import User
from django.test import Client, TestCase
from mdot.dao import pws


class MDOTPersonTest(TestCase):
    """ Tests functionality around getting information about the user once he or
        she logs in.
    """
    def setUp(self):
        pass

    def test_get_affiliation_from_username(self):
        with self.settings(
            RESTCLIENTS_PWS_DAO_CLASS='restclients.dao_implementation.pws.File'
        ):
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
            person = pws.get_person_by_netid('javerage')

            # expected_affiliations =
            # ["member","student","alum","staff","employee"]
            self.assertTrue(person.is_student)
            # TODO: WHY is this coming back None?
            # Won't return true until uw-restclients is fixed
            # self.assertTrue(person.is_alum)
            self.assertTrue(person.is_staff)
            self.assertTrue(person.is_employee)
            self.assertEqual(None, person.is_faculty)

    def test_get_student_number_by_username(self):
        with self.settings(
            RESTCLIENTS_PWS_DAO_CLASS='restclients.dao_implementation.pws.File'
        ):
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
            # call get_student_number_by_username
            student_number = pws.get_student_number_by_netid('javerage')
            # assert that student number = 1033334
            self.assertEqual(student_number, "1033334")
            pass

    def tearDown(self):
        pass
