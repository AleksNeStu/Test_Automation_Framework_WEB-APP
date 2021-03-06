#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Describing of the Contact model."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from sys import maxsize


class Contact:
    """Class that represent model for Contact."""
    def __init__(self, id=None, first_name=None, middle_name=None,
                 last_name=None, address=None, email=None, email2=None,
                 email3=None, home_phone=None, mobile_phone=None,
                 work_phone=None, secondary_phone=None, full_name_home=None,
                 all_emails_home=None, all_phones_home=None,
                 full_name_details=None, all_emails_details=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.full_name_home = full_name_home
        self.all_emails_home = all_emails_home
        self.all_phones_home = all_phones_home
        self.full_name_details = full_name_details
        self.all_emails_details = all_emails_details

    def __repr__(self):
        return ("id:{id}, first_name:{first_name}, middle_name:{middle_name}, "
                "last_name:{last_name}, address:{address}, email:{email}, "
                "email2:{email2}, email3:{email3}, home_phone:{home_phone}, "
                "mobile_phone:{mobile_phone}, work_phone:{work_phone}, "
                "secondary_phone:{secondary_phone}, "
                "full_name_home:{full_name_home}, "
                "all_emails_home:{all_emails_home}, "
                "all_phones_home: {all_phones_home}, "
                "full_name_details:{full_name_details}, "
                "all_emails_details: {all_emails_details}").format(
            id=self.id, first_name=self.first_name, last_name=self.last_name,
            middle_name=self.middle_name, address=self.address,
            email=self.email, email2=self.email2, email3=self.email3,
            home_phone=self.home_phone, mobile_phone=self.mobile_phone,
            work_phone=self.work_phone, secondary_phone=self.secondary_phone,
            full_name_home=self.full_name_home,
            all_emails_home=self.all_emails_home,
            all_phones_home=self.all_phones_home,
            full_name_details=self.full_name_details,
            all_emails_details=self.all_emails_details)

    def __eq__(self, other):
        return (self.id == other.id and self.first_name == other.first_name and
                self.middle_name == other.middle_name and
                self.last_name == other.last_name and
                self.address == other.address and self.email == other.email and
                self.email2 == other.email2 and self.email3 == other.email3 and
                self.home_phone == other.home_phone and
                self.mobile_phone == other.mobile_phone and
                self.work_phone == other.work_phone and
                self.secondary_phone == other.secondary_phone and
                self.full_name_home == other.full_name_home and
                self.all_emails_home == other.all_emails_home and
                self.all_phones_home == other.all_phones_home and
                self.full_name_details == other.full_name_details and
                self.all_emails_details == other.all_emails_details)

    @staticmethod
    def id_or_max(contact):
        """Method to sorted contact objects by id or max value."""
        if contact.id: return int(contact.id)
        else: return maxsize