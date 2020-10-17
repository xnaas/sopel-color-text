# coding=utf8
"""sopel-rainbow-plus

A Sopel plugin to make things rainbow colored or to distribute freedom.
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


class RainbowPlusSection(types.StaticSection):
    order = types.ListAttribute('order', default=[4, 7, 8, 3, 12, 2, 6])
    """The order of color codes to use.

    Defaults to a standard ROYGBIV rainbow (assuming readers' clients use
    typical IRC color code mappings).
    """
    random_start = types.ValidatedAttribute('random_start', bool, default=False)
    """Whether to randomize the start color."""


def configure(config):
    config.define_section('rainbow', RainbowPlusSection)
    config.rainbow.configure_setting(
        'rainbow',
        'Specify the order of IRC color codes to use in the "rainbow":'
    )
    config.rainbow.configure_setting(
        'random_start',
        'Randomize start position in the rainbow?'
    )

class USASection(types.StaticSection):
    order = types.ListAttribute('order', default=[4, 0, 2])
    """USA! USA!"""

def setup(bot):
    bot.config.define_section('rainbow', RainbowPlusSection)


@module.commands('rainbow')
def rainbow_cmd(bot, trigger):
    """Make text into a rainbow."""
    text = clean(trigger.group(2))

    if text == None:
        bot.reply("I can't make a rainbow out of nothing!")
        return module.NOLIMIT

    colors = bot.config.rainbow.order
    color_cycle = itertools.cycle(colors)

    if bot.config.rainbow.random_start:
        for _ in range(len(colors)):
            next(color_cycle)

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
