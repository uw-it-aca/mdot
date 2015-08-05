"""
Tests for the mdot client app.
"""

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import resolve
from mdot.mdot_rest_client.client import MDOT, ClientResource


class MdotClientTest(TestCase):

    def setUp(self):
        pass

    def test_get_resources(self):
        """
        Tests getting JSON from the uwresources API and converting it into a
        class object for use in our templates.
        """
        with self.settings(
            RESTCLIENTS_MDOT_DAO_CLASS='mdot.mdot_rest_client.client.MDOTFile'
        ):
            resources = MDOT().get_resources()
            # Make sure what we get back is a list
            self.assertEqual(type(resources), type([]))
            # Make sure that the first object in the list is of object
            # type ClientResource

            # -> Make sure that we get back the bare minimum fields
            # that we need to make mdot work

            # title: Make sure that the title is unicode
            self.assertEqual(type(resources[0].title), type(u'unicode string'))

            # feature_desc: Make sure that the description is unicode
            self.assertEqual(type(resources[0].feature_desc), type(u'unicode'))

            # image: Make sure that the url is unicode
            self.assertEqual(type(resources[0].image_url), type(u'unicode'))

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

    # Make sure that if there is no image url in the returned json, the
    # image_url in the ClientResource is set to an empty string
    def test_image_is_none(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': None,
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
        image = resources[0].image_url
        # assert that image_url is a string
        self.assertEquals(type('string'), type(image))
        # assert that image_url is an empty string
        self.assertEquals('', image)

    # Make sure that the dict of resource links in the ClientResource
    # is correct when there is one resource
    def test_clientresource_dict_one_resource(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': None,
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
        dict = resources[0].resource_links
        self.assertEqual({u'WEB': u'http://www.washington.edu/itconnect'}, dict)

    # Make sure that the dict of resource links in the ClientResource
    # is correct when there is more than one resource
    def test_clientresource_dict_two_resources(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'This is a test',
                      u'title': u'ITConnect',
                      u'image': None,
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
                      u'campus_tacoma': False},
                     {u'accessible': False,
                      u'feature_desc': u'This is a second test.',
                      u'title': u'SpaceScout',
                      u'image': None,
                      u'created_date': u'2015-07-31T19:18:43.771637Z',
                      u'campus_seattle': True,
                      u'campus_bothell': True,
                      u'responsive_web': True,
                      u'featured': True,
                      u'last_modified': u'2015-07-31T19:21:07.562924Z',
                      u'intended_audiences': [{u'audience': u'student'},
                                              {u'audience': u'staff'},
                                              {u'audience': u'faculty'},
                                              {u'audience': u'freshman'}],
                      u'resource_links':
                          [{u'url': u'http://spacescout.uw.edu',
                            u'link_type': u'WEB'},
                           {u'url': u'http://apple.com',
                            u'link_type': u'IOS'}],
                      u'id': 2,
                      u'campus_tacoma': True}]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        first_dict = resources[0].resource_links
        second_dict = resources[1].resource_links
        self.assertEqual(
            {u'WEB': u'http://www.washington.edu/itconnect'},
            first_dict)
        self.assertEqual(
            {u'WEB': u'http://spacescout.uw.edu', u'IOS': u'http://apple.com'},
            second_dict)

    def test_add_resource_link(self):
        fake_links = [{u'url': u'http://spacescout.uw.edu',
                       u'link_type': u'WEB'},
                      {u'url': u'http://apple.com',
                       u'link_type': u'IOS'}]
        resource = ClientResource(
            u'SpaceScout',
            u'This is a test.',
            None,
            [{u'url': u'bad url', u'link_type': u'BAD'}])
        links = resource.add_resource_link(fake_links)
        self.assertEqual(
            {u'WEB': u'http://spacescout.uw.edu', u'IOS': u'http://apple.com'},
            links)

    def tearDown(self):
        pass


class MdotTest(TestCase):

    # Test that given url calls correct view
    def test_home_url(self):
        resolver = resolve('/')
        self.assertEqual('home', resolver.view_name)

    # Test that given url returns a 200 status code
    def test_home_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
