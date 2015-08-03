from restclients.dao import MY_DAO
from restclients.dao_implementation.mock import get_mockdata_url
import json


class MDOT_DAO(object):
    class File(object):
        """
        The File DAO implementation returns generally static content.  Use this
        DAO with this configuration:
        RESTCLIENTS_MDOT_DAO_CLASS = \
        'mdot.mdot_rest_client.client.MDOT_DAO.File'
        """
        def getURL(self, url, headers):
            return get_mockdata_url("mdot", "file", url, headers)


class MDOT(MY_DAO):
    """
    Put a comment here.
    """
    def get_resources(self):
        response = self.getURL('/api/v1/uwresources',
                               {'Accept': 'application/json'})
        resources = json.loads(response.data)
        resources = self._python_list_to_resources_model_list(resources)
        return resources

    def _python_list_to_resources_model_list(self, resources):
        client_resources = []
        for resource in resources:
            client_resource = ClientResource(resource['title'], resource['feature_desc'], resource['image'])
            for link in resource['resource_links']:
                client_resource.add_resource_link(link['link_type'], link['url'])
            client_resources.append(client_resource)
        return client_resources

    def getURL(self, url, headers):
        return self._getURL('mdot', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_MDOT_DAO_CLASS', MDOT_DAO.File)


class ClientResource(object):
    title = None
    feature_desc = None
    image = None
    resource_links = {}

    def __init__(self, title, feature_desc, image):
        if isinstance(title, unicode):
            self.title = title
        else:
            raise TypeError
        if isinstance(feature_desc, unicode):
            self.feature_desc = feature_desc
        else:
            raise TypeError
        if isinstance(image, unicode):
            self.image = image
        else:
            raise TypeError

    def add_resource_link(self, link_type, url):
        if isinstance(url, unicode) and isinstance(link_type, unicode):
            self.resource_links['link_type'] = url
        else:
            raise TypeError
