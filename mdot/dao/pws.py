"""
This module encapsulates the interactions with the restclients.pws,
provides identity information
"""
from restclients.pws import PWS


def get_person_by_netid(netid):
    person = PWS().get_person_by_netid(netid)
    return person
