# -*- coding: iso-8859-1 -*-
"""
    Process all *.svg files in the repository and update the rdf:about property
    using the supplied base_uri and the relative path.

    Args:

    * base_uri (string): The base URI to be prepended to the file paths

    Example usage:

      python set_uri.py https://raw.github.com/OGCMetOceanDWG/WorldWeatherSymbols/master

    .. note::

        The following XML tag will be updated <cc:Work rdf:about="">

"""

import os
import sys
import warnings

from lxml import etree

def svg_file_list():
    """Returns a list of all svg files with their relative paths"""

    svg_list = []
    for root, dirs, files in os.walk('..'):
        for svgfile in files:
            basename, extension = os.path.splitext(svgfile)
            if extension == '.svg':
                svg_list.append(os.path.abspath(os.path.join(root, svgfile)))
    return svg_list


def modify_uri(base_uri, svg_file):
    """
        Read the entire contents of svg_file, find the row containing the
        rdf:about tag and update with the full URI

        Args:

        * base_uri (string): The base URI to be prepended to the file paths
        * svg_file (string): Relative path to the SVG file

        Returns boolean to indicate success
    """

    success = False

    try:
        parser = etree.XMLParser(remove_blank_text=True)
        svg = etree.parse(svg_file, parser)
        ccwork = svg.find('{http://www.w3.org/2000/svg}metadata/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF/{http://creativecommons.org/ns#}Work')
        ccwork.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about'] = os.path.join(base_uri, os.path.basename(svg_file))
        success = True
    except Exception, err:
        warnings.warn('Could not set rdf:About tag on file %s: %s' % (svg_file, err))

    if success:
        try:
            with open(svg_file, 'w') as output_file:
                output_file.write(etree.tostring(svg, pretty_print=True,
                                  xml_declaration=True, encoding='UTF-8'))
        except Exception, err:
            success = False
            warnings.warn('Could not write update to file %s: %s' %
                          (svg_file, err))
    return success


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s <base_uri>' % sys.argv[0]
        sys.exit(1)

    base_uri = sys.argv[1]

    successes = 0
    failures = 0

    for svg_file in svg_file_list():
        if modify_uri(base_uri, svg_file):
            successes += 1
        else:
            failures += 1

    total = successes + failures

    print '%d files processed.' % total
    print '%d files sucessfully modified.' % successes
    print '%d files failed to be updated.' % failures
