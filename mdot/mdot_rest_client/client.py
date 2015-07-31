from restclients.dao import MY_DAO
from restclients.dao_implementation.mock import get_mockdata_url
import json


class MDOT_DAO(object):
    class File(object):
        """
        The File DAO implementation returns generally static content.  Use this
        DAO with this configuration:
        RESTCLIENTS_MDOT_DAO_CLASS = 'mdot.mdot_rest_client.client.MDOT_DAO.File'
        """
        def getURL(self, url, headers):
            return get_mockdata_url("mdot", "file", url, headers)


class MDOT(MY_DAO):
    """
    Put a comment here.
    """
    def get_resources(self):
        response = self.getURL('/api/v1/uwresources', {'Accept': 'application/json'})
        resources = self._json_to_resources_list(response)
        return resources

    def _json_to_resources_list(self, response):
        resources = json.loads(response.data)
        return resources

    def getURL(self, url, headers):
        return self._getURL('mdot', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_MDOT_DAO_CLASS', MDOT_DAO.File)
