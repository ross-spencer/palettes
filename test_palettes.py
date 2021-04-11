#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test runner for the palettes module."""

from __future__ import print_function

from .palettes import Palettes


def test_palettes_output():
    """The main issue we have when we create a new palette is that the
    structure isn't setup correctly and so an exception will be raised
    somewhere. These tests just make sure that we return some fairly sensible
    information.
    """
    palette = Palettes()
    p_ = palette.get_palette()

    # A palette is a named tuple.
    assert isinstance(p_, tuple)

    # PainterGoblin always uses five colors.
    assert len(p_[1]) == 5

    # Each color is an RGB value.
    for color in p_[1]:
        assert len(color) == 3
        assert color[0] >= 0 and color[0] <= 255
        assert color[1] >= 0 and color[0] <= 255
        assert color[2] >= 0 and color[0] <= 255

    # The label should probably not be blank.
    assert p_[0] != ""
