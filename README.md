image2thermal
=============

A python script for converting images to the format required for printing on ESC/P compatible thermal printers using the "compressed bit image" command.

For example, if your serial port is correctly configured do something like:
    ./image2thermal.py filename.png > /dev/ttyUSB0
