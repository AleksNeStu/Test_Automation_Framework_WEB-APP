#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for modification contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data
from tests.generator.generic import random_data as r_data
from tests.model.contact import Contact


def test_modify_name_of_first_contact(app):
    """Check the possibility of modifying contact's name."""
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_list_of_contacts()
    new_contact_name = Contact(name=r_data(data.CONTACT_NAME_NEW))
    app.contact.modify_first_contact(new_contact_name)
    new_contacts = app.contact.get_list_of_contacts()
    assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact(app):
    """Check the possibility of modifying contact's name, email."""
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_list_of_contacts()
    new_contact = Contact(name=r_data(data.CONTACT_NAME_NEW),
                          last_name=r_data(data.CONTACT_NAME_LAST_NEW),
                          email=r_data(data.CONTACT_EMAIL_NEW))
    app.contact.modify_first_contact(new_contact)
    new_contacts = app.contact.get_list_of_contacts()
    assert len(old_contacts) == len(new_contacts)