#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Modules for providing the web-app's entities's (objects's) attributes."""
"""Describing of the Group model."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from sys import maxsize


class Group:
    """Group model entity."""
    def __init__(self, id=None, name=None, header=None, footer=None):
        self.id = id
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return ("id:{id}, name:{name}, header:{header}, footer:{footer}").format(
            id=self.id, name=self.name, header=self.header, footer=self.footer)

    def __eq__(self, other):
        return (self.id == other.id and self.name == other.name)

    @staticmethod
    def id_or_max(group):
        """Method to sorted group objects by id or max value."""
        if group.id: return int(group.id)
        else: return maxsize