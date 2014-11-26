# -*- coding: iso-8859-1 -*-
"""
Automagically generate MapServer SYMBOL [1] objects from all SVG files

[1] http://mapserver.org/mapfile/symbol.html

Args: None

Example usage:

To create MapServer pixmap symbol objects:

$ python gen_mapserver_symbols.py png > wmo_symbols.sym

To create MapServer svg symbol objects:

# NOTE: MapServer requires libsvg-cairo to support SVG symbols
$ python gen_mapserver_symbols.py svg > wmo_symbols.sym

"""

import os
import sys
import warnings

import xml.etree.ElementTree as etree


def gen_symbols(path, symbol_format='png'):
    """returns SYMBOL objects as string"""

    symbols = ''
    symbol_type = 'pixmap'

    if symbol_format not in ['png', 'svg']:
        raise RuntimeError('format must be png or svg')

    if symbol_format == 'svg':
        symbol_type = symbol_format

    for root, dirs, files in os.walk(os.path.abspath(path)):
        for wwsfile in files:
            basename, extension = os.path.splitext(wwsfile)
            if extension == '.svg':
                if symbol_format == 'svg':
                    filepath = os.path.join(root, wwsfile)
                elif symbol_format == 'png':
                    filepath = '%s%s%s.png' % (os.path.join(path, 'png'),
                                               os.sep, basename)

                try:
                    svg = etree.parse(os.path.join(root, wwsfile))
                    title = svg.find('{http://www.w3.org/2000/svg}title').text
                    symbols += '''
 SYMBOL # %s
  NAME "%s"
  TYPE %s
  IMAGE "%s"
 END
''' % (title.encode('utf8'), basename, symbol_type, filepath)

                except Exception, err:
                    warnings.warn('Could not parse file %s: %s' %
                                  (os.path.join(root, wwsfile), err))
    return symbols

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s <png|svg>' % sys.argv[0]
        sys.exit(0)

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

    print gen_symbols(path, sys.argv[1])
