# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase, override_settings
from mdot.mdot_rest_client.client import MDOT
import json

DAO = 'Mock'


@override_settings(RESTCLIENTS_MDOT_DAO_CLASS=DAO)
class MdotClientRequestTest(TestCase):

    def setUp(self):
        pass

    def test_get_all_resources(self):
        """
        Tests getting JSON from the uwresources API and converting it into a
        class object for use in our templates.
        """
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
        self.assertEqual(len(resources), 3)

    def test_get_resources_by_featured(self):
        """
        Tests retrieval of resources by filtering on attributes.
        """
        resources = MDOT().get_resources(featured=True)
        # make a request separately to ?featured=true
        response = MDOT().getURL('/api/v1/uwresources/?featured=True',
                                 {'Accept': 'application/json'})
        # assert a 200 status
        self.assertEqual(response.status, 200)
        comparison_data = json.loads(response.data)

        # assert that the two retrieved resources have the same id as the
        # ones in the response
        id_list = []
        for item in comparison_data:
            id_list.append(item['id'])
        for resource in resources:
            self.assertTrue(resource.resource_id in id_list)

        # assert the same number of items are returned (and no extras)
        self.assertEqual(comparison_data.__len__(), resources.__len__())

    def test_get_resources_by_multiple_attrs(self):
        """
        WILL TEST retrieval of resources filtered by more than one attribute.
        """
        resources = MDOT().get_resources(featured=True, audience='alumni')
        # make a request separately to ?featured=true&audience=alumni
        url = '/api/v1/uwresources/?featured=True&audience=alumni'
        response = MDOT().getURL(url,
                                 {'Accept': 'application/json'})
        # assert a 200 status
        self.assertEqual(response.status, 200)
        comparison_data = json.loads(response.data)

        # assert that the two retrieved resources have the same id as the
        # ones in the response
        id_list = []
        for item in comparison_data:
            id_list.append(item['id'])
        for resource in resources:
            self.assertTrue(resource.resource_id in id_list)

        # assert the same number of items are returned (and no extras)
        self.assertEqual(comparison_data.__len__(), resources.__len__())
