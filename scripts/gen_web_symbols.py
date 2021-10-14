"""
Automagically generate web friendly svg for specified directory. Can also
strip filename to create shorter symbol id.  Could save a few more bytes by
minifying. The advantage here is that the combined svg file can be retrieved
one time in your html and used multiple times in the same page. Additionally,
once retrieved, the browser should cache it and reduce the number of calls in
the future.

Using the example usage below, you could then reference ww_11 in html like:

<svg xmlns="http://www.w3.org/2000/svg"><use xlink:href="/path/to/file/ww_PresentWeather.svg#ww_11"></use></svg>  # noqa

Args: symbols directory, basename replacement

Example usage:

$ python gen_web_symbols.py ww_PresentWeather WeatherSymbol_WMO_PresentWeather_ > ww_PresentWeather.svg  # noqa

"""

import os
import sys
import warnings

import xml.etree.ElementTree as etree


def gen_symbols(path, strip):
    """returns bloated svg as stripped down symbol"""

    symbols = ''
    svg_namespace = 'http://www.w3.org/2000/svg'
    etree.register_namespace('', svg_namespace)

    for root, dirs, files in os.walk(os.path.abspath(path)):
        for wwsfile in files:
            basename, extension = os.path.splitext(wwsfile)
            if extension == '.svg':
                filepath = os.path.join(root, wwsfile)
                try:
                    svg = etree.parse(filepath)
                    svg_root = svg.getroot()

                    attribs = svg_root.attrib
                    desc = svg.find('{'+svg_namespace+'}desc')
                    svg_root.remove(desc)
                    title = svg.find('{'+svg_namespace+'}title')
                    svg_root.remove(title)
                    metadata = svg.find('{'+svg_namespace+'}metadata')
                    svg_root.remove(metadata)

                    viewbox_attrib = 'viewBox'
                    if viewbox_attrib in attribs:
                        viewbox = attribs[viewbox_attrib]
                    else:
                        viewbox = f"0 0 {attribs['width']} {attribs['height']}"

                    basename2 = basename.replace(strip, '')
                    symbols += f'<symbol id="{basename2}" viewBox="{viewbox}">'

                    for element in svg_root:
                        symbols += etree.tostring(element).decode('utf-8')
                    symbols += '</symbol>'

                except Exception as err:
                    warnings.warn(f'Could not parse file {filepath}: {err}')

    return symbols


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <symbols-dir> <basename-replacement>')
        sys.exit(1)

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'symbols', sys.argv[1])

    print('<svg xmlns="http://www.w3.org/2000/svg">')
    print(gen_symbols(path, sys.argv[2]))
    print('</svg>')
