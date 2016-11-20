#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Application fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from selenium.webdriver.chrome.webdriver import WebDriver
from session import SessionHelper
from group import GroupHelper
from contact import ContactHelper
from open import OpenHelper


class Application():
    """Class for represent Application."""
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.open = OpenHelper(self)

    def destroy(self):
        """Web driver quit method."""
        self.wd.quit()

    def check_fixture_valid(self):
        """Fixture validation."""
        try:
            self.wd.current_url
            return True
        except:
            return False