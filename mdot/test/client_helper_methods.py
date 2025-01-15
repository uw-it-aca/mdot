# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase, Client
from django.urls import resolve
from mdot.mdot_rest_client.client import MDOT, ClientResource
import json


class MdotClientMethodsTest(TestCase):
    # Make sure that has_ios returns true if the resource has an iOS link
    def test_if_has_ios_true(self):
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
                        "link_type": "IOS",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertTrue(resources[0].has_ios())

    # Make sure that has_ios returns false if the resource doesn't
    # have an iOS link
    def test_if_has_ios_false(self):
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
                        "link_type": "WEB",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertFalse(resources[0].has_ios())

    # Make sure that has_and returns true if the resource has an android link
    def test_if_has_and_true(self):
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
                        "link_type": "AND",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertTrue(resources[0].has_and())

    # Make sure that has_and returns false if the resource doesn't
    # have an android link
    def test_if_has_and_false(self):
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
                        "link_type": "WEB",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertFalse(resources[0].has_and())

    # Make sure that has_wip returns true if the resource has a
    # windows phone link
    def test_if_has_wip_true(self):
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
                        "link_type": "WIP",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertTrue(resources[0].has_wip())

    def test_if_has_web_true(self):
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
                        "link_type": "WEB",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertTrue(resources[0].has_web())

    def test_if_has_web_false(self):
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
                        "link_type": "IOS",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertFalse(resources[0].has_web())

    # Make sure that has_wip returns false if the resource
    # doesn't have a windows phone link
    def test_if_has_wip_false(self):
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
                        "link_type": "WEB",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertFalse(resources[0].has_wip())

    def test_if_has_native_true(self):
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
                        "link_type": "WIP",
                    }
                ],
                "id": 1,
                "campus_tacoma": False,
            }
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertTrue(resources[0].has_native())

    # Make sure that if there is no image url in the returned json, the
    # image_url in the ClientResource is set to an empty string
    def test_image_is_none(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "This is a test",
                "title": "ITConnect",
                "image": None,
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
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        image = resources[0].image_url
        # assert that image_url is a string
        self.assertEquals(type("string"), type(image))
        # assert that image_url is an empty string
        self.assertEquals("", image)

    # Make sure that the dict of resource links in the ClientResource
    # is correct when there is one resource
    def test_clientresource_dict_one_resource(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "This is a test",
                "title": "ITConnect",
                "image": None,
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
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        dict = resources[0].resource_links
        self.assertEqual({"WEB": "http://www.washington.edu/itconnect"}, dict)

    # Make sure that the dict of resource links in the ClientResource
    # is correct when there is more than one resource
    def test_clientresource_dict_two_resources(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "This is a test",
                "title": "ITConnect",
                "image": None,
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
            },
            {
                "accessible": False,
                "feature_desc": "This is a second test.",
                "title": "SpaceScout",
                "image": None,
                "created_date": "2015-07-31T19:18:43.771637Z",
                "campus_seattle": True,
                "campus_bothell": True,
                "responsive_web": True,
                "featured": True,
                "last_modified": "2015-07-31T19:21:07.562924Z",
                "intended_audiences": [
                    {"audience": "student"},
                    {"audience": "staff"},
                    {"audience": "faculty"},
                    {"audience": "freshman"},
                ],
                "resource_links": [
                    {"url": "http://spacescout.uw.edu", "link_type": "WEB"},
                    {"url": "http://apple.com", "link_type": "IOS"},
                ],
                "id": 2,
                "campus_tacoma": True,
            },
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        first_dict = resources[0].resource_links
        second_dict = resources[1].resource_links
        self.assertEqual(
            {"WEB": "http://www.washington.edu/itconnect"}, first_dict
        )
        self.assertEqual(
            {"WEB": "http://spacescout.uw.edu", "IOS": "http://apple.com"},
            second_dict,
        )

    def test_add_resource_link(self):
        fake_links = [
            {"url": "http://spacescout.uw.edu", "link_type": "WEB"},
            {"url": "http://apple.com", "link_type": "IOS"},
        ]
        resource = ClientResource(
            1,
            "SpaceScout",
            "This is a test.",
            None,
            [{"url": "bad url", "link_type": "BAD"}],
        )
        links = resource.add_resource_link(fake_links)
        self.assertEqual(
            {"WEB": "http://spacescout.uw.edu", "IOS": "http://apple.com"},
            links,
        )

    def test_resource_order(self):
        fake_list = [
            {
                "accessible": False,
                "feature_desc": "This is a second test.",
                "title": "SpaceScout",
                "image": None,
                "created_date": "2015-07-31T19:18:43.771637Z",
                "campus_seattle": True,
                "campus_bothell": True,
                "responsive_web": True,
                "featured": True,
                "last_modified": "2015-07-31T19:21:07.562924Z",
                "intended_audiences": [
                    {"audience": "student"},
                    {"audience": "staff"},
                    {"audience": "faculty"},
                    {"audience": "freshman"},
                ],
                "resource_links": [
                    {"url": "http://spacescout.uw.edu", "link_type": "WEB"},
                    {"url": "http://apple.com", "link_type": "IOS"},
                ],
                "id": 2,
                "campus_tacoma": True,
            },
            {
                "accessible": False,
                "feature_desc": "AThis is a test",
                "title": "ITConnect",
                "image": None,
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
            },
        ]
        resources = MDOT()._python_list_to_resources_model_list(fake_list)
        self.assertEqual(resources[0].title, "ITConnect")
        self.assertEqual(resources[1].title, "SpaceScout")

    def tearDown(self):
        pass
