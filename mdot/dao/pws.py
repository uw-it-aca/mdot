"""
This module encapsulates the interactions with the restclients.pws,
provides identity information
"""
from restclients.pws import PWS
from restclients.dao import PWS_DAO
import json


PERSON_PREFIX = '/identity/v1/person'


def get_person_by_netid(netid):
    person = PWS().get_person_by_netid(netid)
    return person


def get_data_by_netid(netid):
    dao = PWS_DAO()
    url = "%s/%s/full.json" % (PERSON_PREFIX, netid)
    response = dao.getURL(url, {"Accept": "application/json"})
    return json.loads(response.data)


def get_student_number_by_netid(netid):
    person_data = get_data_by_netid(netid)
    return (person_data["PersonAffiliations"]
                       ["StudentPersonAffiliation"]
                       ["StudentNumber"])
