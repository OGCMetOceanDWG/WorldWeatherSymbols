# -*- coding: iso-8859-1 -*-
#!/usr/bin/python

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


def svg_file_list():
    """
        Returns a list of all svg files with their relative paths

    """
    svg_list = []
    for root, dirs, files in os.walk('.'):
        # Exclude the git database folder
        if root.find('.git') < 0:
            # Remove the initial ./ from the root path
            root = root[2:]
            files = [file_ for file_ in files if file_.endswith(".svg")]
            for svg_file in files:
                svg_list.append(os.path.join(root, svg_file))
    return svg_list


def modify_uri(base_uri, svg_file):
    """
        Read the entire contents of svg_file, find the row containing the
        rdf:about tag and update with the full URI

        Args:

        * base_uri (string): The base URI to be prepended to the file paths
        * svg_file (string): Relative path to the SVG file

        Returns boolen to indicate success

    """
    success = False

    with open(svg_file, 'r') as svg_fh:
        contents = svg_fh.readlines()

    for line_num, line in enumerate(contents):
        tag_start = line.find("<cc:Work")
        if tag_start >= 0:
            # Check for the end bracket of the tag '>', if it exists then
            # store the remaining chars to the appended to the end of the
            # modified line. Note, if the original tag was split across
            # multiple lines then we assume it was only on two lines.
            tag_end = line.find(">", tag_start)
            if tag_end < 0:
                warn_msg = ('The URI tag was split across multiple lines' +
                            ' in ' + svg_file + '\n')
                warnings.warn(warn_msg)
                # Attempting to fix by removing the second line.
                del contents[line_num + 1]
                ending = ''
            else:
                ending = line[tag_end+1:]

            # Modify the line
            beginning = line[:tag_start]
            contents[line_num] = (
                beginning + '<cc:Work rdf:about="' +
                os.path.join(base_uri, svg_file) +
                '">' + ending + '\n')
            success = True
            break

    if success:
        with open(svg_file, 'w') as svg_fh:
            svg_fh.writelines(contents)

    return success


if __name__ == "__main__":
    base_uri = sys.argv[1]

    successes = 0
    failures = 0

    for svg_file in svg_file_list():
        if modify_uri(base_uri, svg_file):
            successes += 1
        else:
            failures += 1

    total = successes + failures
    print str(total), "files processed."
    print str(successes), "files sucessfully modified."
    print str(failures), "files failed to be updated."
