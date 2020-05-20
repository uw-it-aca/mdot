from commonconf import settings

from restclients_core.dao import DAO

from os.path import abspath, dirname
import os
import json


class MDOT(DAO):
    """
    DAO with methods for getting uwresources from the mdot-rest API.
    Uses Mock DAO with following configuration:
    RESTCLIENTS_MDOT_DAO_CLASS='Mock'
    """
    def get_resources(self, **kwargs):
        url = "/api/v1/uwresources/"
        i = kwargs.__len__()
        if kwargs:
            url += "?"
            for key, value in kwargs.items():
                url += "{0}={1}".format(key, value)
                if i > 1:
                    url += "&"
                i = i - 1

        response = self.getURL(url,
                               {'Accept': 'application/json'})
        resources = json.loads(response.data)
        resources = self._python_list_to_resources_model_list(resources)
        return resources

    def _python_list_to_resources_model_list(self, resources):
        client_resources = []
        for resource in resources:
            client_resource = ClientResource(resource['id'],
                                             resource['title'],
                                             resource['feature_desc'],
                                             resource['image'],
                                             resource['resource_links'])
            client_resources.append(client_resource)
            client_resources = sorted(
                client_resources,
                key=lambda client_resource: client_resource.title)
        return client_resources

    def service_name(self):
        return 'mdot'

    def service_mock_paths(self):
        path = [abspath(os.path.join(dirname(__file__), "../resources"))]
        return path

    def get_default_service_setting(self, key):
        if key == "HOST":
            return settings.RESTCLIENTS_MDOT_HOST


class ClientResource(object):
    """
    A class object to be used in the mdot client views.
    """
    resource_id = None
    title = None
    feature_desc = None
    image_url = None
    resource_links = {}

    def __init__(self, resource_id, title, feature_desc, image, links):
        if isinstance(resource_id, int):
            self.resource_id = resource_id
        else:
            raise TypeError("resource_id is not an int: {0}".format(
                            resource_id))
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("title is not unicode: {0}".format(title))
        if isinstance(feature_desc, str):
            self.feature_desc = feature_desc
        else:
            raise TypeError("feature_desc is not unicode: {0}".format(
                            feature_desc))
        if isinstance(image, str):
            self.image_url = image
        elif image is None:
            self.image_url = u''
        else:
            raise TypeError("image_url is not unicode: {0}".format(image))
        self.resource_links = self.add_resource_link(links)

    def add_resource_link(self, links):
        resource_links = {}
        for link in links:
            if isinstance(link['link_type'], str) and\
               isinstance(link['url'], str):
                resource_links[link['link_type']] = link['url']
            else:
                raise TypeError("Error with resource_links: {0}".format(links))
        return resource_links

    def has_ios(self):
        for link in self.resource_links:
            if link == 'IOS':
                return True
        return False

    def has_and(self):
        for link in self.resource_links:
            if link == 'AND':
                return True
        return False

    def has_wip(self):
        for link in self.resource_links:
            if link == 'WIP':
                return True
        return False

    def has_web(self):
        for link in self.resource_links:
            if link == 'WEB':
                return True
        return False

    def has_native(self):
        return self.has_ios or self.has_and or self.has_wip
