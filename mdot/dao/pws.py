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
