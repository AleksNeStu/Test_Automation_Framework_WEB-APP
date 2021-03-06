#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for deleting groups."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from constants import messages, repeat
from model.group import Group


@pytest.mark.smoke_tests
def test_del_some_group(
        app, generator_entities_GroupFactory_generate_create_empty,
        generator_templates_groups):
    """Check of a possibility to delete random group via groups page."""
    group = generator_templates_groups
    if app.group.count_of_groups_groups() == 0:
        app.group.create_group_groups(group)
    first_groups = app.group.list_of_groups_groups()
    ind = randrange(len(first_groups))
    app.group.delete_group_groups(ind)
    assert len(first_groups) - 1 == app.group.count_of_groups_groups()
    actual_groups = app.group.list_of_groups_groups()
    expected_groups = first_groups[:ind] + first_groups[(ind + 1):]
    assert (expected_groups == actual_groups,
            messages.COMPARE_EXP_VS_GOT.format(expected_groups, actual_groups))


@pytest.mark.smoke_tests
def test_del_all_groups(
        app, generator_entities_GroupFactory_generate_create_empty,
        generator_templates_groups):
    """Check of a possibility to delete all groups via groups page."""
    group = generator_templates_groups
    if app.group.count_of_groups_groups() == 0:
        [app.group.create_group_groups(group) for _ in
         xrange(repeat.CREATE_OBJS)]
    app.group.delete_all_groups_groups()
    actual_groups = app.group.list_of_groups_groups()
    assert len(actual_groups) == app.group.count_of_groups_groups() == 0