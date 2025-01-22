# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from mdot.mdot_rest_client.client import MDOT, ClientResource


class MdotClientErrorTest(TestCase):
    def test_get_resource_by_id(self):
        """
        WILL TEST retrieval of a resource by it's id.
        """
        with self.settings(RESTCLIENTS_MDOT_DAO_CLASS="Mock"):
            pass

    def test_python_list_conversion_bad_id(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "IT goodness for the UW",
                "title": 123,
                "image": "http://localhost:8000/\
                      media/uploads/screenshot_CprR5Dk.jpg",
                "created_date": "2015-07-31T19:18:43.771637Z",
                "campus_seattle": True,
                "campus_bothell": False,
                "responsive_web": False,
                "featured": True,
                "last_modified": "2015-07-31T19:21:07.562924Z",
                "intended_audiences": [
                    {"audience": "student"},
                    {"audience": "staff"},
                    {"audience": "faculty"},
                    {"audience": "freshman"},
                ],
                "resource_links": [
                    {
                        "url": "http://www.washington.edu/itconnect",
                        "link_type": "WEB",
                    }
                ],
                "id": "some string not an int",
                "campus_tacoma": False,
            }
        ]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_title(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "IT goodness for the UW",
                "title": 234,
                "image": "http://localhost:8000/\
                      media/uploads/screenshot_CprR5Dk.jpg",
                "created_date": "2015-07-31T19:18:43.771637Z",
                "campus_seattle": True,
                "campus_bothell": False,
                "responsive_web": False,
                "featured": True,
                "last_modified": "2015-07-31T19:21:07.562924Z",
                "intended_audiences": [
                    {"audience": "student"},
                    {"audience": "staff"},
                    {"audience": "faculty"},
                    {"audience": "freshman"},
                ],
                "resource_links": [
                    {
                        "url": "http://www.washington.edu/itconnect",
                        "link_type": "WEB",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_desc(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": 1234,
                "title": "ITConnect",
                "image": "http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg",
                "created_date": "2015-07-31T19:18:43.771637Z",
                "campus_seattle": True,
                "campus_bothell": False,
                "responsive_web": False,
                "featured": True,
                "last_modified": "2015-07-31T19:21:07.562924Z",
                "intended_audiences": [
                    {"audience": "student"},
                    {"audience": "staff"},
                    {"audience": "faculty"},
                    {"audience": "freshman"},
                ],
                "resource_links": [
                    {
                        "url": "http://www.washington.edu/itconnect",
                        "link_type": "WEB",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_image(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "This is a test",
                "title": "ITConnect",
                "image": 123,
                "created_date": "2015-07-31T19:18:43.771637Z",
                "campus_seattle": True,
                "campus_bothell": False,
                "responsive_web": False,
                "featured": True,
                "last_modified": "2015-07-31T19:21:07.562924Z",
                "intended_audiences": [
                    {"audience": "student"},
                    {"audience": "staff"},
                    {"audience": "faculty"},
                    {"audience": "freshman"},
                ],
                "resource_links": [
                    {
                        "url": "http://www.washington.edu/itconnect",
                        "link_type": "WEB",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_link_url(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "This is a test",
                "title": "ITConnect",
                "image": "http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg",
                "created_date": "2015-07-31T19:18:43.771637Z",
                "campus_seattle": True,
                "campus_bothell": False,
                "responsive_web": False,
                "featured": True,
                "last_modified": "2015-07-31T19:21:07.562924Z",
                "intended_audiences": [
                    {"audience": "student"},
                    {"audience": "staff"},
                    {"audience": "faculty"},
                    {"audience": "freshman"},
                ],
                "resource_links": [{"url": 123, "link_type": "WEB"}],
                "id": 1,
                "campus_tacoma": False,
            }
        ]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)

    def test_python_list_conversion_bad_link_type(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "This is a test",
                "title": "ITConnect",
                "image": "http://localhost:8000/media/\
                      uploads/screenshot_CprR5Dk.jpg",
                "created_date": "2015-07-31T19:18:43.771637Z",
                "campus_seattle": True,
                "campus_bothell": False,
                "responsive_web": False,
                "featured": True,
                "last_modified": "2015-07-31T19:21:07.562924Z",
                "intended_audiences": [
                    {"audience": "student"},
                    {"audience": "staff"},
                    {"audience": "faculty"},
                    {"audience": "freshman"},
                ],
                "resource_links": [
                    {
                        "url": "http://www.washington.edu/itconnect",
                        "link_type": 123,
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]

        with self.assertRaises(TypeError):
            MDOT()._python_list_to_resources_model_list(fake_list)
