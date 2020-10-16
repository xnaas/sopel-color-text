# coding=utf8
"""sopel-rainbow

A Sopel plugin to make things RAINBOW COLORED.
"""
from __future__ import unicode_literals, absolute_import, division, print_function

from collections import deque
import unicodedata

from sopel import formatting, module
from sopel.config import types


class RainbowSection(types.StaticSection):
    order = types.ListAttribute('order', default=[4, 7, 8, 3, 12, 2, 6])
    """The order of color codes to use.

    Defaults to a standard ROYGBIV rainbow (assuming readers' clients use
    typical IRC color code mappings).
    """


def configure(config):
    config.define_section('rainbow', RainbowSection)
    config.rainbow.configure_setting(
        'rainbow',
        'Specify the order of IRC color codes to use in the "rainbow":'
    )


def setup(bot):
    bot.config.define_section('rainbow', RainbowSection)


@module.commands('rainbow')
def rainbow_cmd(bot, trigger):
    """Make text into a rainbow."""
    # TODO: Use `formatting.plain()` once Sopel 7.1 is out
    text = trigger.group(2)

    if text == None:
        bot.reply("I can't make a rainbow out of nothing!")
        return module.NOLIMIT

    colors = deque(bot.config.rainbow.order)

    rainbow_text = ''
    for char in text:
        if unicodedata.category(char) == 'Zs':
            # don't color whitespace; there's no point
            rainbow_text += char
        else:
            rainbow_text += formatting.color(char, colors[0])
            colors.rotate(-1)

    bot.say(rainbow_text)
