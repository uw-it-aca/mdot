from django.conf import settings
from restclients.dao import MY_DAO
from restclients.dao_implementation.mock import get_mockdata_url
from restclients.dao_implementation.live import get_con_pool, get_live_url
import json


class MDOTFile(object):
    """
    The File DAO implementation returns generally static content.  Use this
    DAO with this configuration:
    RESTCLIENTS_MDOT_DAO_CLASS = \
    'mdot.mdot_rest_client.client.MDOTFile'
    """
    def getURL(self, url, headers):
        return get_mockdata_url("mdot", "file", url, headers)


class MDOTLive(object):
    """
    This DAO provides real data.  It requires further configuration, e.g.
    RESTCLIENTS_MDOT_DAO_CLASS = \
    'mdot.mdot_rest_client.client.MDOTLive',
    RESTCLIENTS_MDOT_HOST = 'http://yourhost/'
    """
    pool = None

    def getURL(self, url, headers):
        if MDOTLive.pool is None:
            MDOTLive.pool = get_con_pool(settings.RESTCLIENTS_MDOT_HOST)

        return get_live_url(MDOTLive.pool, 'GET',
                            settings.RESTCLIENTS_MDOT_HOST,
                            url,
                            headers=headers,
                            service_name='mdot')


class MDOT(MY_DAO):
    """
    Put a comment here.
    """
    def get_resources(self):
        response = self.getURL('/api/v1/uwresources/',
                               {'Accept': 'application/json'})
        resources = json.loads(response.data)
        resources = self._python_list_to_resources_model_list(resources)
        return resources

    def _python_list_to_resources_model_list(self, resources):
        client_resources = []
        for resource in resources:
            client_resource = ClientResource(resource['title'],
                                             resource['feature_desc'],
                                             resource['image'],
                                             resource['resource_links'])
            client_resources.append(client_resource)
        return client_resources

    def getURL(self, url, headers):
        return self._getURL('mdot', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_MDOT_DAO_CLASS', MDOTFile)


class ClientResource(object):
    title = None
    feature_desc = None
    image = None
    resource_links = {}

    def __init__(self, title, feature_desc, image, links):
        if isinstance(title, unicode):
            self.title = title
        else:
            raise TypeError("title is not unicode: {0}".format(title))
        if isinstance(feature_desc, unicode):
            self.feature_desc = feature_desc
        else:
            raise TypeError("feature_desc is not unicode: {0}".format(
                            feature_desc))
        if isinstance(image, unicode):
            self.image = image
        elif image is None:
            self.image = ''
        else:
            raise TypeError("image is not unicode: {0}".format(image))
        self.add_resource_link(links)

    def add_resource_link(self, links):
        self.resource_links.clear()
        for link in links:
            if isinstance(link['link_type'], unicode) and\
               isinstance(link['url'], unicode):
                self.resource_links[link['link_type']] = link['url']
            else:
                raise TypeError("Error with resource_links: {0}".format(links))

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
