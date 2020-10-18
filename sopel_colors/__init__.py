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

COLOR_SCHEMES = {
    'rainbow': [4, 7, 8, 3, 12, 2, 6],
    'usa':     [4, 0, 2],
    'commie':  [0, 2, 4],
    'spooky':  [8, 7, 0],
}

@module.commands('rainbow', 'usa', 'commie', 'spooky')
def rainbow_cmd(bot, trigger):
    """Make text colored."""
    text = clean(trigger.group(2))

    if text == None:
        bot.reply("I can't work with nothing!")
        return module.NOLIMIT

    scheme = trigger.group(1).lower()
    try:
        colors = COLOR_SCHEMES[scheme]
    except KeyError:
        # not possible to reach this at time of writing, but who knows?
        # mistakes happen when updating stuff that needs to be changed in parallel
        bot.reply("I don't know what color sequence to use for '{}'!".format(scheme))
        return module.NOLIMIT

    color_cycle = itertools.cycle(colors)

    bot.say(
        ''.join(
            char if unicodedata.category(char) == 'Zs'
            else formatting.color(char, next(color_cycle))
            for char in text
        )
    )
