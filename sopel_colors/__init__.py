# coding=utf8
"""sopel-color-text

A Sopel plugin to add some colored text options.
"""
from __future__ import unicode_literals, absolute_import, division, print_function

import itertools
import random
import unicodedata

from sopel import formatting, module
from sopel.config import types

# Remove when dropping support for Sopel < 7.1
if hasattr(formatting, 'plain'):
    clean = formatting.plain
else:
    clean = lambda t: t

class RainbowSection(types.StaticSection):
    order = types.ListAttribute('order', default=[4, 7, 8, 3, 12, 2, 6])
    """The order of color codes to use.

    Defaults to a standard ROYGBIV rainbow (assuming readers' clients use
    typical IRC color code mappings)."""

class USASection(types.StaticSection):
    order = types.ListAttribute('order', default=[4, 0, 2])
    """USA! USA!"""

class CommieSection(types.StaticSection):
    order = types.ListAttribute('order', default=[0, 2, 4])
    """God damn commies."""

class SpookySection(types.StaticSection):
    order = types.ListAttribute('order', default=[8, 7, 0])
    """Spooky! 👻"""

def setup(bot):
    bot.config.define_section('rainbow', RainbowSection)
    bot.config.define_section('usa', USASection)
    bot.config.define_section('commie', CommieSection)
    bot.config.define_section('spooky', SpookySection)

@module.commands('rainbow')
def rainbow_cmd(bot, trigger):
    """Make text into a rainbow."""
    text = clean(trigger.group(2))

    if text == None:
        bot.reply("I can't make a rainbow out of nothing!")
        return module.NOLIMIT

    colors = bot.config.rainbow.order
    color_cycle = itertools.cycle(colors)

    bot.say(
        ''.join(
            char if unicodedata.category(char) == 'Zs'
            else formatting.color(char, next(color_cycle))
            for char in text
        )
    )

@module.commands('usa')
def usa_cmd(bot, trigger):
    """Distribute FREEDOM."""
    text = clean(trigger.group(2))

    if text == None:
        bot.reply("I can't distribute FREEDOM out of nothing!")
        return module.NOLIMIT

    colors = bot.config.usa.order
    color_cycle = itertools.cycle(colors)

    bot.say(
        ''.join(
            char if unicodedata.category(char) == 'Zs'
            else formatting.color(char, next(color_cycle))
            for char in text
        )
    )

@module.commands('commie')
def commie_cmd(bot, trigger):
    """Racist commie command."""
    text = clean(trigger.group(2))

    if text == None:
        bot.reply("I need text to commie-ize!")
        return module.NOLIMIT

    colors = bot.config.commie.order
    color_cycle = itertools.cycle(colors)

    bot.say(
        ''.join(
            char if unicodedata.category(char) == 'Zs'
            else formatting.color(char, next(color_cycle))
            for char in text
        )
    )

@module.commands('spooky')
def spooky_cmd(bot, trigger):
    """Racist commie command."""
    text = clean(trigger.group(2))

    if text == None:
        bot.reply("I need text to spookify!")
        return module.NOLIMIT

    colors = bot.config.commie.order
    color_cycle = itertools.cycle(colors)

    bot.say(
        ''.join(
            char if unicodedata.category(char) == 'Zs'
            else formatting.color(char, next(color_cycle))
            for char in text
        )
    )
