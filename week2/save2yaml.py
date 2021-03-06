#!/usr/bin/env python
# save2yaml.py
# Claudia
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "8/13/16  3:06 PM"
__copyright__ = "Copyright (c) 2015 Claudia de Luna"
__license__ = "Python"

import sys

#sys.path.append("/Users/Claudia/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetA/")

import telnet_test
import yaml


# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    Description
    :return:
    """
    data = dict(
        A = 'a',
        B = dict(
            C = 'c',
            D = 'd',
            E = 'e',
        ),
        C = [1,2,3,4,5],
        D = {'router':'cisco ASR', 'interface': "Gi0"}
    )

    with open('dataFalse.yml', 'w') as outfile:
        #yaml.dump(data, outfile, default_flow_style=True)
        yaml.dump(data, outfile)

    print("Importing the telnet_test.py module in this script: " + sys.argv[0])
    print(telnet_test.currwkdir())

# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print '\nUsage: save2yaml.py - No arguments are passed\nExample: python save2yaml.py\n\n'
        sys.exit()
    else:
        main()

