[![Build Status](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols/workflows/build%20%E2%9A%99%EF%B8%8F/badge.svg)](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols)

WorldWeatherSymbols
===================

A complete set of WMO weather symbols in SVG with full metadata

Download
--------

The full repository sources are available at https://github.com/OGCMetOceanDWG/WorldWeatherSymbols.git

Accessing the symbols
---------------------

### Pre-generated PNGs

A set of pre-generated PNGs are available for download at https://github.com/OGCMetOceanDWG/WorldWeatherSymbols/releases/download/0.6.0/WorldWeatherSymbols-0.6.0-png.zip.

### Building PNGs

To build PNG equivalents of the symbols, run ```./scripts/wws_manage.sh png```.  Output PNG files are located in ```png/```.  [Inkscape](https://inkscape.org) is required to run the conversions.  

Viewing the symbols
---------------------

### The symbols and their descriptions

A list of symbols with their filenames and associated descriptions is provided in [symbols subfolders](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols/tree/master/symbols/) in the respective README.md files ([example for the Ft_Fronts subfolder](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols/tree/master/symbols/Ft_Fronts/)). Those README.md files are generated automatically by the [wws_manage.sh](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols/tree/master/scripts/wws_manage.sh) script. These lists act a short guides to the WMO WorldWeatherSymbols.


### Displaying the symbols on GitHub

WorldWeatherSymbols can be displayed directly on Github either by opening the symbol's svg file or by using [RawGit](https://rawgit.com/) to include symbols in Markdown-formatted files, example: ![Front_Cold_at_surface](https://cdn.rawgit.com/OGCMetOceanDWG/WorldWeatherSymbols/master/symbols/Ft_Fronts/WeatherSymbol_WMO_Front_Quasi-stationary_at_surface.svg).

Version history
---------------------

See [HISTORY.txt](https://github.com/OGCMetOceanDWG/WorldWeatherSymbols/tree/master/HISTORY.txt)
