# sopel-color-text

A Sopel plugin to make some silly colored text. Mostly stolen from sopel-rainbow.

## Dependencies

Only Sopel itself, version 7.0 or higher.

If installed on a bot using Sopel 7.1+, `sopel-color-text` will strip control
codes from the input text before applying the rainbow colors. (Sopel 7.0.x
does not offer this feature, so feeding formatted text into the `.rainbow`
command might yield unexpected results.)

This version of `sopel-color-text` will not work with Sopel 9.0+.
A future release might correct this, sometime before Sopel 9 becomes stable.
