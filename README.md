[![Build Status](https://travis-ci.org/OGCMetOceanDWG/WorldWeatherSymbols.png?branch=master)](https://travis-ci.org/OGCMetOceanDWG/WorldWeatherSymbols)

WorldWeatherSymbols
===================

A complete set of WMO weather symbols in SVG with full metadata and fallback PNGs.

V01 First complete WMO set, copied from web, and completed with Inkscape with Inkscapisms, in a variety of coordinates.

V02 Complete WMO set, with consistent coordinates, mainly 55x55.

V03 Complete WMO set, consistent coordinates, but all Inkscapisms removed in a batch process.

V04 Complete WMO set, changed all svg tags to svg namespace, rather than blank/nonamespace. Removed remaining Inkscape references. Used global edits in Notepad++.

V05 Complete WMO set with standard metadata block in each symbol and correct metadata detail, including uris of files in Github. Removed explicit mention of "uri:".

Removed spurious DESC and TITLE elements. If more than one valid WMO description, put extra in DESC element, hierarchically, separated by colons.

Created extra table entry references needed for variations allowed by plotting model but not necessarily in Manual on Codes tables. E.g. Automatic station.

Suppressed style information in filenames, such as "monochromatic", as this is a presentation style, not semantic.

Added Aviation symbols.

TBD:

Remove unnecessary deep grouping? I suggest each symbol is in a single group, rather than each in its own SVG?

Remove unnecessary transformations?

Remove unnecessary precision?

This could all remain as Version 5, as every files contains its version number in the metadata.

I suggest that V06 would be a different resolution, such as 100x100 or 20x20, or with optional styles encoded, or significant extra symbols added.
