"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from mdot.mdot_rest_client.client import MDOT


class MdotClientTest(TestCase):
    def setUp(self):
        pass

    def test_get_resources(self):
        """
        Tests the client that retrieves data from the mdot API.
        """
        # TODO: make sure to patch settings to always use file
        # based for unit tests
        resources = MDOT().get_resources()
        # Make sure what we get back is a list
        self.assertEqual(type(resources), type([]))
        # Make sure that the first object in the list is of object
        # type ClientResource

        # -> Make sure that we get back the bare minimum fields
        # that we need to make mdot work

        # title: Make sure that the title is unicode
        self.assertEqual(type(resources[0].title), type(u'string'))

        # feature_desc: Make sure that the description is unicode
        self.assertEqual(type(resources[0].feature_desc), type(u'string'))

        # image: Make sure that the url is unicode
        self.assertEqual(type(resources[0].image), type(u'string'))

        # resource_links: Make sure that the resource links are in a dict
        self.assertEqual(type(resources[0].resource_links), type({}))
        self.assertEqual(len(resources), 2)

    def test_python_list_conversion_bad_title(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'IT goodness for the UW',
                      u'title': 234,
                      u'image': u'http://localhost:8000/\
                      media/uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'WEB'}],
                      u'id': 1,
                      u'campus_tacoma': False}]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_desc(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': 1234,
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'WEB'}],
                      u'id': 1,
                      u'campus_tacoma': False}]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_image(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': 'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'WEB'}],
                      u'id': 1,
                      u'campus_tacoma': False}]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_link_url(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': 'http://www.washington.edu/itconnect',
                            u'link_type': u'WEB'}],
                      u'id': 1,
                      u'campus_tacoma': False}]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_link_type(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': 'WEB'}],
                      u'id': 1,
                      u'campus_tacoma': False}]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    # Make sure that has_ios returns true if the resource has an iOS link
    def test_if_has_ios_true(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'IOS'}],
                      u'id': 1,
                      u'campus_tacoma': False}]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertTrue(resources[0].has_ios())

    # Make sure that has_ios returns false if the resource doesn't
    # have an iOS link
    def test_if_has_ios_false(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'WEB'}],
                      u'id': 1,
                      u'campus_tacoma': False}]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertFalse(resources[0].has_ios())

    # Make sure that has_and returns true if the resource has an android link
    def test_if_has_and_true(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'AND'}],
                      u'id': 1,
                      u'campus_tacoma': False}]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertTrue(resources[0].has_and())

    # Make sure that has_and returns false if the resource doesn't
    # have an android link
    def test_if_has_and_false(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'WEB'}],
                      u'id': 1,
                      u'campus_tacoma': False}]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertFalse(resources[0].has_and())

    # Make sure that has_wip returns true if the resource has a
    # windows phone link
    def test_if_has_wip_true(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'WIP'}],
                      u'id': 1,
                      u'campus_tacoma': False}]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertTrue(resources[0].has_wip())

    # Make sure that has_wip returns false if the resource
    # doesn't have a windows phone link
    def test_if_has_wip_false(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': u'http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg',
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': False,
                      u'responsive_web': False,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://www.washington.edu/itconnect',
                            u'link_type': u'WEB'}],
                      u'id': 1,
                      u'campus_tacoma': False}]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertFalse(resources[0].has_wip())

    def tearDown(self):
        pass
