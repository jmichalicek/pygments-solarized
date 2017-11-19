# -*- coding: utf-8 -*-
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, Number, Operator, Generic, Literal, Text

BASE0 = '#839496'
BASE1 = '#93a1a1'
BASE2 = '#eee8d5'
BASE3 = '#fdf6e3'
BASE00 = '#657b83'
BASE01 = '#586e75'
BASE02 = '#073642'
BASE03 = '#002b36'
YELLOW = '#b58900'
# ORANGE = '#cb4b16'
RED = '#dc322f'
MAGENTA = '#d33682'
VIOLET = '#6c71c4'
BLUE = '#268bd2'
CYAN = '#2aa198'
GREEN = '#859900'


BASE0 = '#FFFFFF'  # Not sure about this.  Just taking guesses
BASE2 = '#45515F'
WHITE = '#FFFFFF'  # regular text
ORANGE = '#DF691A'  # stuff...
LIGHT_ORANGE = '#F0AD4E'  # comments


class SolarizedStyle(Style):

    """ Light version solarized theme (http://ethanschoonover.com/solarized). """
    background_color = BASE2
    styles = {
        Text: 'bg: %s %s' % (BASE2, BASE01),
        Keyword: ORANGE,
        Keyword.Constant: 'bold',
        # Keyword.Declaration
        Keyword.Namespace: RED + ' bold',
        # Keyword.Pseudo
        # Keyword.Reserved
        Keyword.Type: 'bold',
        Name: BLUE,
        # Name.Attribute
        Name.Builtin: ORANGE,
        # Name.Builtin.Pseudo
        Name.Class: ORANGE,
        Name.Tag: 'bold',
        Literal: CYAN,
        # String
        Number: 'bold',
        # Operator
        Operator.Word: GREEN,
        Comment: LIGHT_ORANGE + ' italic',
        Generic: MAGENTA,
    }
#     styles = {
#         Text: 'bg: %s %s' % (BASE2, BASE01),
#         Keyword: GREEN,
#         Keyword.Constant: 'bold',
#         # Keyword.Declaration
#         Keyword.Namespace: RED + ' bold',
#         # Keyword.Pseudo
#         # Keyword.Reserved
#         Keyword.Type: 'bold',
#         Name: BLUE,
#         # Name.Attribute
#         Name.Builtin: ORANGE,
#         # Name.Builtin.Pseudo
#         Name.Class: ORANGE,
#         Name.Tag: 'bold',
#         Literal: CYAN,
#         # String
#         Number: 'bold',
#         # Operator
#         Operator.Word: GREEN,
#         Comment: BASE1 + ' italic',
#         Generic: MAGENTA,
#     }
