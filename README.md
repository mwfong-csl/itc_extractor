## ITC Extractor
This Python2 module extracts images from iTunes ITC files.

Based on the work of [Simon Kennedy](http://www.sffjunkie.co.uk/python-itc.html), this Python2 module extracts images from ITC files.
```
Usage: python2 itc.py [options] filespec

Options:
  -h, --help            show this help message and exit
  -l, --list            list image information and exit.
  -n NUMBER, --number=NUMBER
                        only output image number NUMBER.
  -b BASENAME, --basename=BASENAME
                        base name for output files appended with the image
                        number and extension.
  -d DIRECTORY, --directory=DIRECTORY
                        base directory for output files.
  -a IMGSPEC, --add=IMGSPEC
                        add an image. To specify an image include 3 arguments
                        separated by colons: "<filename>:<width>:<height>"
  -q, --quiet           do not display info when extracting.
```
Running
```
python itc.py -l '..\data\*-D44D96D70B751BA0.itc'
```
produces
```
ITC File Information for ..\data\B8748DAC8262BE49-B59A14EA21FE5400.itc
    Image 01, width=128, height=128, format=PNG, location=local
    Image 02, width=256, height=256, format=PNG, location=local
    Image 03, width=400, height=400, format=PNG, location=local
```
To decode all iTunes `.itc` files on macOS, run
```
mkdir ITC
find ~/Music/iTunes/ -type f -name '*.itc' -exec ln -s {} ITC/ \;
python2 <path to itc_extractor.git/itc/itc.py> 'ITC/*.itc'
```
## Dependencies
None