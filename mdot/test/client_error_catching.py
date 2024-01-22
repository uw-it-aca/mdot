# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from mdot.mdot_rest_client.client import MDOT, ClientResource


class MdotClientErrorTest(TestCase):
    def test_get_resource_by_id(self):
        """
        WILL TEST retrieval of a resource by it's id.
        """
        with self.settings(
            RESTCLIENTS_MDOT_DAO_CLASS='Mock'
        ):
            pass

    def test_python_list_conversion_bad_id(self):
        fake_list = [{u'accessible': False,
                      u'feature_desc': u'IT goodness for the UW',
                      u'title': 123,
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
                      u'id': 'some string not an int',
                      u'campus_tacoma': False}]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

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
                      u'image': 123,
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
                          [{u'url': 123,
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
                            u'link_type': 123}],
                      u'id': 1,
                      u'campus_tacoma': False}]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)
